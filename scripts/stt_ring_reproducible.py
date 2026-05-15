#!/usr/bin/env python3
"""Reproducible STT ring-road simulation.

This script implements the stochastic Optimal Velocity (OV) ring-road model used
as the numerical validation component of the Socio-Traffic Thermodynamics (STT)
manuscript. It is a minimal illustrative surrogate, not a calibrated traffic model.

Equations implemented:
    dx_i/dt = v_i
    dv_i/dt = a * (V(h_i) - v_i) + sigma_sov * xi_i(t)

The original uploaded working script did not fix a random seed. This cleaned
version exposes a seed so that GitHub/Zenodo users can reproduce a deterministic
representative run. The exact uploaded manuscript figure is preserved separately
as figures/stt_result_original_uploaded.png.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def v_opt(headway: np.ndarray, v_max: float, h_c: float) -> np.ndarray:
    """Optimal Velocity response used in the Bando-style ring surrogate."""
    return v_max * (np.tanh(headway - h_c) + np.tanh(h_c)) / (1.0 + np.tanh(h_c))


def simulate(
    n_vehicles: int = 30,
    road_length: float = 300.0,
    sensitivity: float = 1.0,
    v_max: float = 10.0,
    h_c: float = 5.0,
    dt: float = 0.1,
    steps: int = 3000,
    sigma_sov: float = 0.5,
    seed: int = 20260416,
) -> tuple[np.ndarray, np.ndarray]:
    """Run the stochastic OV ring simulation.

    Returns
    -------
    time : ndarray, shape (steps,)
        Simulation time in seconds.
    history_x : ndarray, shape (steps, n_vehicles)
        Vehicle positions on the periodic ring.
    """
    rng = np.random.default_rng(seed)

    x = np.linspace(0.0, road_length, n_vehicles, endpoint=False)
    v = np.zeros(n_vehicles)
    history_x = np.zeros((steps, n_vehicles))

    for t in range(steps):
        headways = np.roll(x, -1) - x
        headways[-1] += road_length

        noise = rng.normal(0.0, sigma_sov, n_vehicles)
        acceleration = sensitivity * (v_opt(headways, v_max, h_c) - v) + noise

        v = np.maximum(v + acceleration * dt, 0.0)
        x = (x + v * dt) % road_length
        history_x[t] = x

    time = np.arange(steps) * dt
    return time, history_x


def plot_spacetime(
    time: np.ndarray,
    history_x: np.ndarray,
    road_length: float,
    sigma_sov: float,
    out_png: Path,
    dpi: int = 300,
) -> None:
    """Create a space-time diagram, breaking lines at periodic wraparound."""
    out_png.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.style.use("dark_background")

    for i in range(history_x.shape[1]):
        pos = history_x[:, i].copy()
        diff = np.diff(pos)
        pos[:-1][diff < -road_length / 2.0] = np.nan
        plt.plot(time, pos, color="cyan", alpha=0.7, linewidth=1.5)

    plt.xlabel("Time (seconds)", fontsize=12)
    plt.ylabel("Position on Ring Road (meters)", fontsize=12)
    plt.title(
        f"STT: Space-Time Diagram (sovereignty fluctuation = {sigma_sov})",
        fontsize=14,
    )
    plt.tight_layout()
    plt.savefig(out_png, dpi=dpi)
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-vehicles", type=int, default=30)
    parser.add_argument("--road-length", type=float, default=300.0)
    parser.add_argument("--sensitivity", type=float, default=1.0)
    parser.add_argument("--v-max", type=float, default=10.0)
    parser.add_argument("--h-c", type=float, default=5.0)
    parser.add_argument("--dt", type=float, default=0.1)
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--sigma-sov", type=float, default=0.5)
    parser.add_argument("--seed", type=int, default=20260416)
    parser.add_argument("--out", type=Path, default=Path("results/stt_result_seed20260416.png"))
    args = parser.parse_args()

    time, history_x = simulate(
        n_vehicles=args.n_vehicles,
        road_length=args.road_length,
        sensitivity=args.sensitivity,
        v_max=args.v_max,
        h_c=args.h_c,
        dt=args.dt,
        steps=args.steps,
        sigma_sov=args.sigma_sov,
        seed=args.seed,
    )
    plot_spacetime(time, history_x, args.road_length, args.sigma_sov, args.out)
    print(f"Saved {args.out}")


if __name__ == "__main__":
    main()

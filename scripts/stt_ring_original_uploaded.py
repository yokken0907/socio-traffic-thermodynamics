import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. パラメータ設定（ここを後でいじって遊びます）
# ==========================================
N = 30          # 車両数
L = 300.0       # 円環路の長さ (m)
a = 1.0         # ドライバーの反応感度
v_max = 10.0    # 最大速度 (m/s)
h_c = 5.0       # 安全と感じる車間距離 (m)
dt = 0.1        # 1回の計算で進む時間 (秒)
steps = 3000    # シミュレーションの総ステップ数

# ★ 理論の核心：主権揺らぎ（個人の気まぐれ）の強さ
# 0.0 なら全員が機械のように正確に運転し、渋滞は起きません。
# 0.5 程度にすると、人間らしい迷いが生じ、自然渋滞が発生します。
sigma_sov = 0.5 

# ==========================================
# 2. 初期化
# ==========================================
# 車両を円環路に等間隔に配置し、初期速度は全員0とします
x = np.linspace(0, L, N, endpoint=False)
v = np.zeros(N)

# 記録用の配列を用意
history_x = np.zeros((steps, N))

# 最適速度関数 (車間距離に応じて出したい速度を決める関数)
def V_opt(h):
    return v_max * (np.tanh(h - h_c) + np.tanh(h_c)) / (1 + np.tanh(h_c))

# ==========================================
# 3. シミュレーションの実行
# ==========================================
print(f"シミュレーション開始... (主権揺らぎ: {sigma_sov})")

for t in range(steps):
    # 自分の前の車との車間距離を計算 (円環路なので先頭の前の車は最後尾)
    headways = np.roll(x, -1) - x
    headways[-1] += L

    # 加速度の計算 (理想的な追従 ＋ 個人の揺らぎノイズ)
    noise = np.random.normal(0, sigma_sov, N)
    acceleration = a * (V_opt(headways) - v) + noise

    # 速度と位置の更新
    v = v + acceleration * dt
    v = np.maximum(v, 0.0) # 後退はしない
    x = x + v * dt
    x = x % L # 円環路のループ処理

    # 位置を記録
    history_x[t] = x

print("計算完了。グラフを生成します...")

# ==========================================
# 4. グラフ（時空図）の描画と保存
# ==========================================
plt.figure(figsize=(10, 6))
plt.style.use('dark_background') # ダークモードで描画

time_array = np.arange(steps) * dt

# 車両1台ずつの軌跡をプロット
for i in range(N):
    pos = history_x[:, i].copy()
    # 円環路の0m地点をまたぐ際に線が縦に繋がらないようにする処理
    diff = np.diff(pos)
    pos[:-1][diff < -L/2] = np.nan
    plt.plot(time_array, pos, color='cyan', alpha=0.7, linewidth=1.5)

plt.xlabel("Time (seconds)", fontsize=12)
plt.ylabel("Position on Ring Road (meters)", fontsize=12)
plt.title(f"STT Theory: Space-Time Diagram (Sovereignty Fluctuation = {sigma_sov})", fontsize=14)
plt.tight_layout()

# WSL環境でGUIが開かない場合を考慮し、画像ファイルとして保存
file_name = "stt_result.png"
plt.savefig(file_name, dpi=300)
print(f"画像ファイル '{file_name}' として保存しました！")

# 画面にも表示を試みる
plt.show()

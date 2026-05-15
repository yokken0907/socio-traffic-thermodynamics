# Socio-Traffic Thermodynamics (STT)

本リポジトリは、以下の論文と数値検証素材を公開・確認・DOIアーカイブ用に整理した public-gate パッケージです。

**Socio-Traffic Thermodynamics: Congestion as a Non-Equilibrium Dissipative Structure Driven by Social Potential**  
Keiji Yoshimura, Independent Researcher, 2026.

## 収録範囲

本リポジトリは、STT論文のPDFと、論文中の数値検証に対応する最小 stochastic Optimal Velocity ring-road simulation を保存します。

論文の中心は、交通渋滞を、社会的ポテンシャル勾配に沿って移動するエージェントが有限容量・有限帯域の交通ネットワーク上で生成する非平衡散逸構造として捉える理論枠組みです。

数値検証は限定的です。固定ボトルネックのない周期リング道路で、確率的OVモデルが自発的な stop-and-go wave を生成することを示す、最小サロゲート実験です。

## 内容物

- `manuscript/socio_traffic_thermodynamics_2026.pdf` - 論文PDF。
- `scripts/stt_ring_original_uploaded.py` - アップロード元のWSL/Pythonスクリプト。
- `scripts/stt_ring_reproducible.py` - seed指定に対応した整理版スクリプト。
- `figures/stt_result_original_uploaded.png` - 論文の数値検証図に対応するアップロード元画像。
- `results/stt_result_original_uploaded.png` - 元結果画像の保存コピー。
- `docs/PROJECT_CONSISTENCY_AUDIT.md` - 論文とアップロードフォルダの対応確認。
- `CLAIM_BOUNDARY.md` - 主張境界。
- `AI_ASSISTANCE_DISCLOSURE.md` - AI利用明記。
- `FILE_MANIFEST.csv/json` - SHA-256 manifest。

元ZIPには Python 仮想環境 `stt_env/` が丸ごと含まれていましたが、GitHub/Zenodo用途には不適切なため除外しました。依存関係は `requirements.txt` で管理します。

## 技術的ビジュアル案内

初めて本リポジトリを見る技術的関心のある読者向けに、ブラウザだけで開ける技術的ビジュアル案内ページを同梱しています。

`docs/technical_visual_orientation/index.html`

このページは、Socio-Traffic Thermodynamics の transition-diagnosis logic をプロジェクト固有の観点から整理する補助資料です。本リポジトリにおける mission variable は city traffic-control performance、transport-policy success、または universal decongestion ではなく、density/demand、response-delay、interaction、noise 条件の下で free flow、capacity-frontier operation、stop-and-go wave formation、dissipative congestion、blackout-like flow collapse を識別する reduced traffic-flow transition diagnosis です。

また、このページでは reduced socio-traffic surrogate state channels、non-equilibrium / thermodynamic analogy discipline、regime classification、evidence hierarchy、リポジトリ閲覧順、および claim boundary を短く整理しています。主要な図解セクションには replay control を付けており、静的テンプレートではなく診断ロジックを段階的に確認できます。

このページは説明補助であり、traffic-control simulation を実行するものではありません。transportation policy、city-control software、signal-control guidance、universal decongestion、または自治体実装可能性を示すものでもなく、論文本体、source materials、figures、または専門家による独立評価を置き換えるものでもありません。

## 実行例

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/stt_ring_reproducible.py --seed 20260416 --out results/stt_result_seed20260416.png
```

元スクリプトは random seed を固定していなかったため、アップロード元画像のピクセル単位の完全再現は主張しません。元画像は保存し、整理版スクリプトでは再現可能な代表実行を提供します。

## 主張境界

本リポジトリが支持するのは、固定ボトルネックなしの最小 stochastic OV ring-road simulation において、自発的な stop-and-go wave が形成され得るという、サロゲートレベルの限定的主張です。

実交通ネットワークへの較正、政策実装、交通管制システムとしての妥当性、安全重要システムへの導入可能性は主張しません。

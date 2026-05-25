# Socio-Traffic Thermodynamics (STT)

本リポジトリは、以下の論文・数値検証素材・v0.3.0統合補遺を公開確認用に整理した claim-bounded パッケージです。

**Socio-Traffic Thermodynamics: Congestion as a Non-Equilibrium Dissipative Structure Driven by Social Potential**  
Keiji Yoshimura, Independent Researcher, 2026.

この v0.3.0 パッケージでは、元のSTT public-gate 論文と最小リング道路検証素材に加えて、有限容量toy networkにおける **risk-budgeted information release** に関する統合補遺を追加しています。

## 収録範囲

STTは、交通渋滞を、社会的ポテンシャル勾配に沿って移動するエージェントが有限容量・有限帯域の交通ネットワーク上で生成する非平衡散逸構造として捉える理論枠組みです。

元の数値検証は限定的です。固定ボトルネックのない周期リング道路で、確率的OVモデルが自発的な stop-and-go wave を生成することを示す、最小サロゲート実験です。

v0.3.0統合補遺では、高感度・高頻度・同期的な情報反応が有限容量toy network上で過負荷、振動、社会コストを増幅し得るか、また低レート・粗粒化・段階的な情報放出がリスク予算つきの緩衝設計として解釈できるかを、claim-bounded なtoy-model auditとして整理しています。

## 内容物

- `paper/socio_traffic_thermodynamics_2026.pdf` - 元のSTT論文PDF。
- `paper/socio_traffic_thermodynamics_2026.tex` - 元のSTT論文TeXソース。
- `paper/STT_risk_budgeted_information_release_addendum_v0_3_0.pdf` - v0.3.0統合補遺PDF。
- `paper/STT_risk_budgeted_information_release_addendum_v0_3_0.tex` - 補遺TeXソース。
- `scripts/stt_ring_original_uploaded.py` - アップロード元のWSL/Pythonスクリプト。
- `scripts/stt_ring_reproducible.py` - seed指定に対応した整理版スクリプト。
- `figures/stt_result_original_uploaded.png` - 論文の数値検証図に対応するアップロード元画像。
- `results/stt_result_original_uploaded.png` - 元結果画像の保存コピー。
- `evidence/v030_synthesis_outputs/` - v0.3.0統合出力、選択図表、claim lock、phase ledger。
- `docs/PROJECT_CONSISTENCY_AUDIT.md` - 論文とアップロードフォルダの対応確認。
- `CLAIM_BOUNDARY.md` - 主張境界。
- `AI_ASSISTANCE_DISCLOSURE.md` - AI利用明記。
- `LICENSE` および `LICENSE_EVALUATION_ONLY.txt` - ソースライセンス条件。
- `FILE_MANIFEST.csv/json` - SHA-256 manifest。

元ZIPには Python 仮想環境 `stt_env/` が丸ごと含まれていましたが、GitHub/Zenodo用途には不適切なため除外しています。依存関係は `requirements.txt` で管理します。

## 技術的ビジュアル案内

初めて本リポジトリを見る技術的関心のある読者向けに、ブラウザだけで開ける技術的ビジュアル案内ページを同梱しています。

`docs/technical_visual_orientation/index.html`

このページは説明補助であり、traffic-control simulation を実行するものではありません。transportation policy、city-control software、signal-control guidance、universal decongestion、または自治体実装可能性を示すものでもなく、論文本体、evidence、figures、または専門家による独立評価を置き換えるものでもありません。

## 元リング道路サロゲートの実行例

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/stt_ring_reproducible.py --seed 20260416 --out results/stt_result_seed20260416.png
```

元スクリプトは random seed を固定していなかったため、アップロード元画像のピクセル単位の完全再現は主張しません。元画像は保存し、整理版スクリプトでは再現可能な代表実行を提供します。

## v0.3.0 locked synthesis result

v0.3.0統合補遺では、以下のtoy-model結果をロックしています。

```text
Best frozen holdout policy: budget_common_u0.055_s0.00
Mean cost: 1.734372
No-information mean cost: 1.758804
Improvement vs no-information: 0.024432
Delta overload severity vs no-information: -0.004088
```

解釈としては、検証済みの有限容量toy-network条件内では、高感度・同期的な情報反応が過負荷と社会コストを増幅し得る一方で、低レート・risk-budgeted な情報放出は、frozen holdout auditにおいて no-information null より平均コストを下げ、overload severityを増やさない候補として成立しました。

## 主張境界

本リポジトリが支持するのは、toy model / surrogate レベルの限定的主張のみです。以下は主張しません。

- 実交通ネットワークへの較正
- 実交通予測精度
- 交通政策としての実証済み有効性
- 都市スケール実装可能性
- 万能な渋滞解消方法
- 安全重要交通管制システムへの導入可能性
- 全ての渋滞が同一機構から生じることの証明
- 既存の交通流理論・交通計画・ネットワーク経路選択モデルの代替

## ライセンス

本リポジトリは、`LICENSE` および `LICENSE_EVALUATION_ONLY.txt` に記載した独自の **Evaluation-Only Public License Notice** に基づきます。

Zenodoでは、CC-BY-NC-4.0ではなく、ソース側ライセンスを参照する独自/その他open license扱いが適切です。`.zenodo.json` では `other-open` とし、ライセンス条件はリポジトリ内の `LICENSE` / `LICENSE_EVALUATION_ONLY.txt` を参照する形にしています。

## Zenodo-safe citation handling

GitHub/Zenodoアーカイブ用のメタデータとして、以下をルートに含めています。

- `CITATION.cff`
- `.zenodo.json`

Zenodo release作成時、既存の `10.5281/zenodo.xxxxx` を external DOI欄に入力しないでください。ZenodoにこのGitHub release用の新しい repository-archive DOI を自動生成させます。既存 DOI `10.5281/zenodo.20201218` は履歴上のrepository-archive文脈としてのみ保持します。

## Support

本プロジェクトは、機関スポンサーなしで独立に開発されています。保守・文書化への任意支援については [SUPPORT.md](SUPPORT.md) を参照してください。

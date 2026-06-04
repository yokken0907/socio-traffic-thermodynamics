# Socio-Traffic Thermodynamics (STT)

**有限容量 toy traffic network における stop-and-go wave、同期リスク、risk-budgeted information release を扱う claim-bounded reduced-surrogate archive です。**

Project website: https://yokken0907.github.io/socio-traffic-thermodynamics/  
Repository: https://github.com/yokken0907/socio-traffic-thermodynamics

## 現在の公開パッケージ

**リポジトリ版:** `v0.3.2-public-landing-and-metadata-refresh`  
**科学本文の基準版:** `v0.3.1-integrated-revision-source-license-checked`  
**今回の更新目的:** 公開入口整理、メタデータ刷新、GitHub Pages 対応、検索導線整備、claim boundary の強化配置。

この v0.3.2 パッケージは、v0.3.1 統合原稿の科学的主張を拡張するものではありません。旧ZIP内で二重化していたリポジトリ構造を解消し、読者が最新版の PDF・主張境界・証拠ファイルに迷わず到達できるように整理した公開用リポジトリです。

## 最初に読むもの

1. Project website / visual orientation: `https://yokken0907.github.io/socio-traffic-thermodynamics/`
2. 統合原稿 PDF: `paper/integrated_v0_3_1/STT_integrated_model_risk_budget_synthesis_v0_3_1.pdf`
3. Claim boundary: `CLAIM_BOUNDARY.md`
4. Reader guidance: `docs/STT_v031_reader_guidance.md`
5. Release note: `docs/release/RELEASE_DATA_v0_3_2.md`

## このリポジトリの位置づけ

STT は、現実交通政策や実都市交通予測ではなく、toy-model / reduced-surrogate レベルの診断アーカイブです。

含まれる内容は以下です。

- 確率的 ring-road surrogate による内生的 stop-and-go wave の再現。
- 有限容量 toy network における shared information と synchronization risk の audit 出力。
- tested frozen holdout setting に限定された risk-budgeted information-release 診断。
- v0.3.1 統合原稿と evidence package。

意図する利用は、有限容量・同期・過負荷リスク・情報提示の関係を考えるための **仮説生成的・診断的資料** です。

## 主張しないこと

本リポジトリは、以下を主張しません。

- 現実交通の予測精度。
- 交通政策の妥当性検証。
- 実都市交通計画への適用可能性。
- 経路誘導・交通制御システムとしての実装準備性。
- 安全認証済み交通管理手法。
- 普遍的な渋滞解消法。
- 現実の運転者に対して交通情報を一般に制限・非公開化すべきという主張。
- 公共交通情報の制限を推奨する政策提案。

情報提示に関する結果は、tested finite-capacity toy networks に限定された synchronization-risk diagnostic として読むべきであり、現実の情報統制・経路誘導政策ではありません。

## GitHub Pages 設定

推奨設定:

```text
Settings → Pages → Build and deployment
Source: Deploy from a branch
Branch: main
Folder: /docs
```

Website欄には以下を設定します。

```text
https://yokken0907.github.io/socio-traffic-thermodynamics/
```

## ライセンス

本リポジトリは `LICENSE` および `LICENSE_EVALUATION_ONLY.txt` に記載された source-defined **Evaluation-Only Public License Notice** を使用します。

Zenodo では CC-BY-NC-4.0 ではなく、Other / source-defined / license in repository / other-open 相当として扱ってください。本パッケージの `.zenodo.json` には DOI を固定記載していません。

## AI利用

構成整理、文章化、リポジトリ再編、claim-boundary 表現の補助に生成AIを利用しています。公開判断、主張境界、内容確認の責任は作成者にあります。詳細は `AI_ASSISTANCE_DISCLOSURE.md` を参照してください。

Author: Keiji Yoshimura, Independent Researcher  
Contact: yokken0907@gmail.com

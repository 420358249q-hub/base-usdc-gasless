# Target decision

## Decision: Candidate A first

| Dimension | A: Base USDC SDK example | B: Solana Chinese Quickstart i18n |
| --- | --- | --- |
| Delivery certainty | High: narrow API surface and deterministic artifact | Medium-high: file scope is clear, but terminology and completeness are subjective |
| CI automation | High: typed-data and transaction construction are fully mockable offline | High for syntax/link checks, but translation coverage needs review tooling or maintainer judgment |
| Maintainer subjectivity | Medium-low: behavior can be checked against EIP-3009 | Medium-high: Chinese wording, terminology, and tone are inherently review-sensitive |
| Anti-spam reputation | Strong signal: useful executable example with tests and safety guardrails | Weaker signal if submitted as a large machine-translated documentation block |

The expected value is better for A despite its lower listed reward in the radar snapshot. The implementation is deliberately dry-run by default and does not claim Base maintainer approval or bounty acceptance.

## Evidence boundary

The local workspace did not contain a checkout of either upstream repository. The included CI proves the standalone example's tests on Python 3.14/web3 7.x; upstream branch rules, exact issue acceptance criteria, and current contract integration still require a human maintainer check before opening a PR.

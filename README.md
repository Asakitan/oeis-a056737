# A056737：中心因数差的平均阶常数

Chain.Ren · 独立研究 · 2026-11-27

上下中心因数的差与最大素因数相差至多 $n^{2/3}$；素数立方表明点态指数是锐的。结合最大素因数的经典平均阶，得到 [A056737](https://oeis.org/A056737) 的准确常数 $\pi^2/6$。

[完整证明](PROOF.md) · [复核脚本](verify.py) · [文献核对](PRIOR.md) · [公开版本](https://github.com/Asakitan/oeis-a056737/releases/tag/proof-v1.0.1) · [引用](CITATION.cff)

运行 `python -B verify.py` 以整数复算 $2\le n\le50000$ 的比较不等式。

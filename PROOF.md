# 最接近的共轭因数之差的平均阶

**署名：** Chain.Ren · 独立研究

**版本：** [proof-v1.0.1](https://github.com/Asakitan/oeis-a056737/releases/tag/proof-v1.0.1) · 2026-11-27（Australia/Sydney）

OpenAI Codex 实质参与了推导、文稿整理和复核。

设 $d(n)$ 是 $n$ 不超过 $\sqrt n$ 的最大正因数，$D(n)=n/d(n)$，$a(n)=D(n)-d(n)$。由于 $n/t-t$ 随正 $t$ 递减，这也是 $n$ 所有正因数对的最小非负差。[OEIS A056737](https://oeis.org/A056737) 记载 Clive Tooth 于 2025 年提出的猜想：$a(n)$ 的平均阶为 $k n/\log n$，并给出 $k$ 的粗略数值估计。

**定理。** 平均阶常数为 $k=\zeta(2)=\pi^2/6$。也就是说，
$$
\lim_{x\to\infty}\frac{\sum_{2\le n\le x}a(n)}
{\sum_{2\le n\le x}n/\log n}=\frac{\pi^2}{6}.
$$
这不是对各个 $n$ 的逐点等价；例如 $n$ 为平方数时差为零。

## 与最大素因数的逐点比较

记 $P(n)$ 为 $n\ge2$ 的最大素因数。我们证明
$$|a(n)-P(n)|\le n^{2/3}.$$

若 $p=P(n)>\sqrt n$，写 $n=mp$，$m<\sqrt n<p$。不含 $p$ 的因数都整除 $m$，含 $p$ 的因数至少为 $p$。因此中心因数对恰为 $(m,p)$，有 $a(n)-P(n)=-m$，其绝对值小于 $\sqrt n$。

若 $P(n)\le\sqrt n$，先找一个落在 $[n^{1/3},n^{2/3}]$ 的因数 $u$。如果 $P(n)\ge n^{1/3}$，取 $u=P(n)$ 即可。否则，把 $n$ 的素因子（计重数）依次相乘，取第一个达到 $n^{1/3}$ 的部分积；之前的积及新乘的素因子都小于 $n^{1/3}$，故所得 $u<n^{2/3}$。由于 $u$ 和 $n/u$ 都处于该区间，较小者不超过 $\sqrt n$ 且不小于 $n^{1/3}$。因此 $d(n)\ge n^{1/3}$，$D(n)\le n^{2/3}$。此时 $a(n)$ 和 $P(n)$ 都位于 $[0,n^{2/3}]$，比较式得证。

点态误差的指数不能统一降至 $2/3-\varepsilon$：对素数立方 $n=p^3$，$a(n)=p^2-p$，从而 $a(n)-P(n)=p^2-2p\sim n^{2/3}$。

## 平均阶

求和得 $\sum_{2\le n\le x}a(n)=\sum_{2\le n\le x}P(n)+O(x^{5/3})$。使用最大素因数的经典渐近式（Knuth–Pardon；也见 Alladi–Erdős；[Naslund, *The Average Largest Prime Factor*, 式 (1)](https://ftp.gwdg.de/pub/misc/EMIS/journals/INTEGERS/papers/n81/n81.pdf)）：
$$
\sum_{2\le n\le x}P(n)\sim\frac{\pi^2}{12}\frac{x^2}{\log x}.
$$
$x^{5/3}$ 对这一主项是低阶量，所以中心因数差有同一求和主项。另一方面 $t/\log t$ 在 $t>e$ 时递增，故求和与对应积分之差为 $O(x/\log x)$；用洛必达法则比较 $\int_2^x t/\log t\,dt$ 与 $x^2/(2\log x)$，二者渐近等价。将两个求和主项相除即得定理。∎

[整数复核](verify.py)检验点态比较及素数立方的锐性例子。极限由上述论证而非有限数值比值决定。

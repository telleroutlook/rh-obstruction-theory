# OB-35 独立审稿裁决：抽象奇亚纯 jet 非可识别性引理

**审稿对象：** `OB-35-Eprime-refined-degree-resend.md`  
**审稿日期：** 2026-08-13  
**最终裁决：** **GATE-A CONDITIONAL**  
**当前稿件状态：** 不得以现有文字直接从 `PROOF-DRAFT` 升为 `INDEPENDENTLY-CHECKED`；完成第 9 节列出的强制修改后，可以仅以“抽象引理、非 Suzuki 目标定理”的身份升级。

---

## 0. 决定性摘要

原稿的核心构造可以成立，且不需要 RH。Link B 的三次项展开和 Cauchy 下界正确；Link A 的真正非零基点 jet-IFT 系统也可闭合。更强的是，原稿未证明的一般非退化性实际上有如下精确公式。

令

\[
s:=\tau^2>0,\qquad
x_\ell:=a_{k+\ell}\ (1\le \ell\le J),\qquad
y_m:=a_{k+J+m}\ (m\ge1).
\]

则沿 jet-IFT 分支有

\[
\boxed{
\Delta_1'(0)
=(-1)^{J+1}2s^J
\sum_{m\ge1}
\frac{y_m\prod_{\ell=1}^J(x_\ell-y_m)}
{(J+m)(1+s y_m)^J}}
\tag{0.1}
\]

其中每个求和项的绝对值严格为正，因为

\[
x_1>\cdots>x_J>y_m>0.
\]

故对所有满足 (A1) 的抽象序列、所有 \(k\ge0\)、\(J\ge1\) 和 \(\tau\ne0\)，都有

\[
\Delta_1'(0)\ne0,
\qquad
\operatorname{sgn}\Delta_1'(0)=(-1)^{J+1}.
\tag{0.2}
\]

于是对每组固定数据，确有 \(c_0>0\)，使 \(0<|c|<c_0\) 时 \(\Delta_1(c)\ne0\)，首个非零次数为 \(d=3\)。

但是，现稿仍有四个必须修复的问题：

1. 它用单一模型 \(\gamma_n=n,k=1,\tau=1\) 且仅 \(J=1,\dots,4\) 的计算，代替了对 (A1) 全量词的证明；这在逻辑上不足。
2. \(J=4\) 的数值锚点错误。严格区间计算给出
   \[
   -9.8470664608\times10^{-7}
   <\Delta_1'(0)<
   -9.8470664433\times10^{-7},
   \]
   并非 \(-1.2\times10^{-6}\)。
3. “每增加一个 \(J\) 约缩小 10 倍”不符合所列模型的实际比值；前三个相邻绝对值比约为 \(23.94,32.61,44.04\)。四个点也不能单独证明一般渐近速率。
4. “degree 不 uniform in \(J\)”的说法不正确。每个固定 \(J\) 的次数均为同一个整数 \(3\)；现有论证只能说未证明统一的 \(J\)-独立小邻域，并且三次项系数没有正的 \(J\)-一致下界。

因此，本裁决不是 BLOCKED：没有发现不可修复的数学反例；但在补入 (0.1) 的一般证明、改正数值和精确定义之前，也不能 PASS。

---

## 1. 审稿边界、量词与依赖

### 1.1 应有的精确量词

原稿的“Under (A1)–(A3), fix \(k,J\), for all sufficiently small \(c<0\)”应展开为：

\[
\begin{aligned}
&\forall(A,B)\text{ 满足 (A1)--(A3)},\ 
\forall k\in\mathbb N_0,\ 
\forall J\in\mathbb N,\\
&\exists\varepsilon=\varepsilon(A,k,J,\tau)>0,\ 
\forall c\in(-\varepsilon,0),\ 
\exists F^{(c)}.
\end{aligned}
\tag{1.1}
\]

这里 \(\varepsilon\) 不得只写成 \(c_0(J)\)，除非 \(A,k,\tau\) 已在该段固定为特定模型。IFT 只给出自由参数 \(u(c)\) 的唯一局部分支，不给出记录类中所有可能 \(F\) 的全局唯一性。

### 1.2 当前定义中的缺口

以下符号在原稿中未达到“自包含、无歧义”标准。

| 项目 | 当前问题 | 必须澄清的形式 |
|---|---|---|
| \(A,B\) | 只称 function/order，未在定义句中明说 entire | 明写“\(A,B\) 为整函数” |
| \(\mathcal E_N^{\rm mer}\) | \(N\) 未定义；“normalization”未定义；“first \(J\) coefficients”索引不明 | 改为 \(\mathcal E_{k,J}^{\rm mer}(w_0)\)，逐条定义 |
| jet | “first \(J\)”可能指 \(0\le j<J\) 或 \(0\le j\le J\) | 明写 \(F^{(j)}(w_0)=W^{(j)}(w_0)\), \(0\le j<J\) |
| normalization | 构造实际保证的是原点线性系数相同 | 明写 \(\lim_{z\to0}F(z)/z=A(0)/\widetilde B(0)\) |
| \(x_\ell,y_m,b_m\) | 在 lemma 前未完整定义 | 明写见第 2 节 |
| \(\Delta_r\) | 只定义了 \(\Delta_1\)，后文却使用 \(\Delta_r\) | 对每个整数 \(q\ge1\) 定义 \(\Delta_q\) |
| “next odd \(r\)” | 下标与幂次数混淆 | 首个非零下标为 \(q\)，次数为 \(2q+1\) |
| \(R_B\) | 若 \(B\) 无非零零点，空集距离未约定 | 约定此时 \(R_B=+\infty\) |

这些不是纯排版问题：若“normalization + first \(J\)”被理解成值归一化外加 \(J\) 个导数条件，就共有 \(J+1\) 个条件，而当前 IFT 只有 \(J\) 个自由变量。

### 1.3 引用核对

1. **内部 OB-09。** 可定位的文件是 `OB-09-E-prime-neg-IFT-odd-meromorphic.md`，相关修正版在 §7.1–§7.2，尤其是式 (7.3)–(7.7)。该文件先裁定旧的幂和系统不能匹配非零 \(w_0\)-jet，再给出当前使用的真正 jet 系统。OB-35 的 Link A 与该修正版一致，但“OB-09-confirmed core”不是作者、年份、定理编号齐全的公开引文，不能替代本稿中的证明。
2. **OB-30。** 当前附件没有给出可核查的作者、年份、文件版本或定理编号。它只能作为修订历史，不能作为证明前提。本裁决没有继承 OB-30 的结论。
3. **Suzuki。** 能与“entire family”精确对应的原始来源是 Masatoshi Suzuki, *A family of deformations of the Riemann xi-function*, Acta Arith. 157 (2013), no. 3, 201–230, DOI [10.4064/aa157-3-1](https://doi.org/10.4064/aa157-3-1)。其 **Theorem 2.2(2)** 断言固定实 \(\alpha\) 时 \(\xi_\alpha(s;r)\) 关于 \((s,r)\) 为整函数，**Theorem 2.2(7)** 给出固定参数时关于 \(s\) 的阶至多为 1。该定理并不陈述“moving-pole convergence”；若原稿保留此说法，必须另行定义收敛拓扑并给出独立轮廓积分论证。
4. **标准结果。** 有限维实 IFT、Rolle 定理和 Cauchy 系数估计均未在原稿中附作者/年份/编号。它们是标准基础定理；本稿逐项核对了它们在此处所需的有限维、可微性、非退化及全纯圆盘假设。没有任何非标准外部定理被当作未核实的黑箱。

---

## 2. 精确定义下的构造

置

\[
t_0=w_0^2=-\tau^2=-s<0,
\quad
x_\ell=a_{k+\ell}\ (1\le\ell\le J),
\quad
y_m=a_{k+J+m}\ (m\ge1),
\tag{2.1}
\]

并定义

\[
b_m(c):=y_m\left(1+\frac{c}{J+m}\right)^{-2}.
\tag{2.2}
\]

正确的扰动乘积是

\[
A_{u,c}(z):=A(0)
\prod_{n=1}^k(1-a_nz^2)
\prod_{\ell=1}^J(1-u_\ell z^2)
\prod_{m\ge1}(1-b_m(c)z^2),
\tag{2.3}
\]

以及

\[
F^{(c)}(z):=\frac{z^2A_{u(c),c}(z)}{B(z)}.
\tag{2.4}
\]

在 \((u,c)=(x,0)\) 和 \(t_0\) 附近取实对数，令

\[
L(t;u,c)
=\sum_{\ell=1}^J\log\frac{1-u_\ell t}{1-x_\ell t}
+\sum_{m\ge1}\log\frac{1-b_m(c)t}{1-y_mt}.
\tag{2.5}
\]

因 \(t_0<0\)、\(x_\ell,y_m>0\)，基点处所有对数因子均为正。又因

\[
\sum_m y_m<\infty,
\qquad
b_m'(0)=-\frac{2y_m}{J+m},
\tag{2.6}
\]

函数级数及所需的 \(t,u,c\) 导数在一个公共邻域内一致收敛；故有限维实 IFT 可用。

定义

\[
\Psi_j(u,c):=\partial_t^jL(t_0;u,c),
\qquad 0\le j<J.
\tag{2.7}
\]

显然 \(\Psi(x,0)=0\)。其 Jacobian 行列式为

\[
\det D_u\Psi(x,0)
=(-t_0)^J\left(\prod_{j=0}^{J-1}j!\right)
\frac{\prod_{1\le p<q\le J}(x_q-x_p)}
{\prod_{\ell=1}^J(1-x_\ell t_0)^J}.
\tag{2.8}
\]

这里 \(-t_0=s>0\)，\(1-x_\ell t_0=1+s x_\ell>0\)，且 \(x_p\ne x_q\)，所以 (2.8) 非零。该公式还以有理算术对 \(J=1,\dots,6\) 的样例矩阵逐项复算过，实际行列式与右端之比均精确等于 1。

IFT 给出唯一局部 \(C^1\) 分支 \(u(c)\)，且

\[
L(t;u(c),c)=O((t-t_0)^J).
\tag{2.9}
\]

由于 \(z\mapsto z^2\) 在 \(w_0\ne0\) 处局部可逆，(2.9) 推出

\[
A_{u(c),c}(z)-A(z)=O((z-w_0)^J),
\tag{2.10}
\]

从而

\[
(F^{(c)})^{(j)}(w_0)=W^{(j)}(w_0),
\qquad 0\le j<J.
\tag{2.11}
\]

### 2.1 记录类成员资格的其余条件

- **奇性：** \(A_{u,c}\) 偶、\(B\) 奇，故 \(z^2A_{u,c}/B\) 为奇亚纯函数。
- **原点归一化：** \(A_{u,c}(0)=A(0)\)，故
  \[
  \lim_{z\to0}\frac{F^{(c)}(z)}z
  =\frac{A(0)}{\widetilde B(0)}
  =\lim_{z\to0}\frac{W(z)}z.
  \]
- **零点：** 缩小 \(c\)-邻域后，有限个自由零点保持正、简单、有序。对 \(c<0\)，\(1+c/(J+m)\) 随 \(m\) 严格递增且为正，故尾部零点也严格有序；连接处由有限间隙和连续性控制。前 \(k\) 个正零点保持为 \(\gamma_1,\dots,\gamma_k\)。
- **极点：** (A2) 使 \(B\) 的非零零点全为非实数，而 \(A\) 和 \(A_{u,c}\) 的零点全为实数。因此两分子都不在 \(B\) 的非零零点消零，\(F^{(c)}\) 与 \(W\) 有完全相同的有限极点及重数。
- **阶：** 新旧零点一致可比，零点收敛指数不变；有限个自由因子不影响阶。因此 \(A_{u,c}\) 仍为阶至多 1 的整函数，商的 Nevanlinna 阶也至多为 1。
- **非恒等：** 对 \(c<0\)，每个尾部零点 \(\mu_{k+J+m}(c)<\gamma_{k+J+m}\)。在已保持严格全序的邻域内，新旧正零点序列不可能逐项相同，故 \(A_{u,c}\not\equiv A\)，从而 \(F^{(c)}\ne W\)。

因此，Link A 的数学核心成立；但必须把这些定义和检查写进当前稿，不能仅写“OB-09 core, unchanged”。

---

## 3. Link B：原点展开、次数与 Cauchy 下界

对每个整数 \(q\ge1\) 定义

\[
\Delta_q(c):=
\sum_{\ell=1}^J\bigl(u_\ell(c)^q-x_\ell^q\bigr)
+\sum_{m\ge1}\bigl(b_m(c)^q-y_m^q\bigr).
\tag{3.1}
\]

这些级数绝对收敛。在原点邻域，

\[
L(t;u(c),c)
=-\sum_{q\ge1}\frac{\Delta_q(c)}q\,t^q.
\tag{3.2}
\]

特别地，\(L(0)=0\) 且 \(L'(0)=-\Delta_1(c)\)。由

\[
A_{u,c}=A\,e^L
\]

得

\[
A_{u,c}(z)-A(z)
=-A(0)\Delta_1(c)z^2+O(z^4).
\tag{3.3}
\]

又

\[
\frac{z^2}{B(z)}
=\frac{z}{\widetilde B(0)}+O(z^3),
\]

故

\[
\boxed{
F^{(c)}(z)-W(z)
=-\frac{A(0)}{\widetilde B(0)}\Delta_1(c)z^3+O(z^5).}
\tag{3.4}
\]

因此

\[
d=3\quad\Longleftrightarrow\quad\Delta_1(c)\ne0.
\tag{3.5}
\]

这也确认旧的 \(z^{2J+3}\) 结论不适用于当前 \(w_0\)-jet 系统：条件 (2.11) 位于 \(w_0\ne0\)，并不令原点幂和 \(\Delta_1,\dots,\Delta_J\) 消失。

更一般地，若

\[
q_0:=\min\{q\ge1:\Delta_q(c)\ne0\},
\]

则

\[
F^{(c)}(z)-W(z)
=-\frac{A(0)}{\widetilde B(0)}
\frac{\Delta_{q_0}(c)}{q_0}z^{2q_0+1}
+O(z^{2q_0+3}).
\tag{3.6}
\]

原稿的“next odd \(r\) with \(\Delta_r\ne0\)”应替换为 (3.6)：\(q_0\) 是正整数下标，不要求是奇数；奇数的是最终次数 \(2q_0+1\)。若所有 \(\Delta_q\) 都为零，则 (3.2) 使 \(L\) 在原点邻域恒零，解析延拓将推出 \(F^{(c)}\equiv W\)，与已证非恒等矛盾。因此某个 \(q_0\) 必存在。

令

\[
R_B:=\operatorname{dist}(0,Z(B)\setminus\{0\}),
\]

并在集合为空时约定 \(R_B=+\infty\)。函数 \(F^{(c)}-W\) 在 \(|z|<R_B\) 全纯。对 \(0<R<R_B\)，Cauchy 系数公式给出

\[
\sup_{|z|=R}|F^{(c)}(z)-W(z)|
\ge
\left|\frac{A(0)}{\widetilde B(0)}\Delta_1(c)\right|R^3.
\tag{3.7}
\]

所以 Link B 除“next odd \(r\)”措辞外成立。

---

## 4. Link C：一般非退化性的独立证明

原稿对单一数值模型的四次计算不能证明全称命题。本节给出缺失的一般证明。

对 jet 方程在 \(c=0\) 求导。由 (2.6)，置

\[
X_\ell:=\frac{x_\ell}{1+s x_\ell},
\qquad
Y_m:=\frac{y_m}{1+s y_m},
\tag{4.1}
\]

\[
\alpha_\ell:=\frac{u_\ell'(0)}{1+s x_\ell},
\qquad
p_m:=\frac{2y_m}{(J+m)(1+s y_m)}>0.
\tag{4.2}
\]

因为 \(L_c(t)=-tR(t)\) 且 \(t_0\ne0\)，\(L_c\) 在 \(t_0\) 有至少 \(J\) 阶零点等价于 \(R\) 有至少 \(J\) 阶零点。逐阶求导得到矩条件

\[
\sum_{\ell=1}^J\alpha_\ell X_\ell^q
=\sum_{m\ge1}p_mY_m^q,
\qquad 0\le q<J.
\tag{4.3}
\]

令 \(I_Xh\) 为在节点 \(X_1,\dots,X_J\) 上的次数至多 \(J-1\) Lagrange 插值多项式，并取

\[
h(X):=\frac1{1-sX}.
\tag{4.4}
\]

由 (4.3)，

\[
\Delta_1'(0)
=\sum_{m\ge1}p_m\bigl((I_Xh)(Y_m)-h(Y_m)\bigr).
\tag{4.5}
\]

对这个有理函数，插值余项可精确写成

\[
h(Y)-(I_Xh)(Y)
=\frac{s^J\prod_{\ell=1}^J(Y-X_\ell)}
{(1-sY)\prod_{\ell=1}^J(1-sX_\ell)}.
\tag{4.6}
\]

将 (4.1)–(4.2) 代入 (4.5)–(4.6)，即得 (0.1)。由于 \(y_m<x_J\)，每一项同号且非零，级数由 \(\sum y_m<\infty\) 绝对收敛。故 (0.2) 成立。

由 \(\Delta_1(0)=0\) 及 (0.2)，

\[
\Delta_1(c)=c\Delta_1'(0)+o(c).
\]

所以对每组固定的 \((A,k,J,\tau)\)，存在 \(c_0>0\)，使 \(0<|c|<c_0\) 时 \(\Delta_1(c)\ne0\)。这才是“每个固定 \(J\)，小 \(c\) 时 \(d=3\)”的完整证明。

---

## 5. 数值锚点的精确/区间算术复核

对原稿指定模型

\[
\gamma_n=n,\quad k=1,\quad w_0=i,\quad s=1,
\]

(0.1) 化为

\[
\Delta_1'(0)=(-1)^{J+1}
2\sum_{n=J+2}^{\infty}
\frac{n^{-2}\prod_{q=2}^{J+1}(q^{-2}-n^{-2})}
{(n-1)(1+n^{-2})^J}.
\tag{5.1}
\]

每个绝对值项都是有理数且为正。审稿计算将 \(n\le N=200000\) 的每一项以精确分数生成，再以 60 位十进制定向舍入累加。尾项使用

\[
0<a_{J,n}
\le
\frac{2\prod_{q=2}^{J+1}q^{-2}}{n^2(n-1)},
\]

以及

\[
\sum_{n>N}\frac1{n^2(n-1)}
\le
\frac1{N^3}+\frac1{2N^2}
\tag{5.2}
\]

作严格外包。所得区间如下。

| \(J\) | \(\Delta_1'(0)\) 的严格包含区间 | 原稿锚点 | 裁决 |
|---:|---:|---:|---|
| 1 | \([0.0338580562594887,\ 0.0338580562657388]\) | \(+0.033858\)；另写 \(0.0338580562\ldots\) | 符合 |
| 2 | \([-0.0014143956591774,\ -0.0014143956584828]\) | \(-0.0014\) | 粗略但符合 |
| 3 | \([0.0000433670888355,\ 0.0000433670888790]\) | \(+4.3\times10^{-5}\) | 粗略但符合 |
| 4 | \([-9.8470664608\times10^{-7},\ -9.8470664433\times10^{-7}]\) | \(-1.2\times10^{-6}\) | **不符合** |

\(J=1\) 时 (5.1) 确实化为原稿所列

\[
\sum_{n\ge3}
\frac{n^2-4}{2n^2(n^2+1)(n-1)},
\]

故其交叉核对正确。

相邻绝对值的实际比值约为

\[
23.9382,qquad32.6145,qquad44.0406,
\]

不是“约 10 倍”。

### 5.1 可证明的非一致性究竟是什么

由 (0.1) 可直接估计

\[
|\Delta_1'(0)|
\le
\frac{2s^J}{J+1}
\left(\prod_{\ell=1}^Jx_\ell\right)
\sum_{m\ge1}y_m.
\tag{5.3}
\]

对固定 \(A,k,\tau\)，右端随 \(J\to\infty\) 趋于 0。因此线性化三次项系数没有正的 \(J\)-一致下界。这不等于次数不一致：次数在每个固定 \(J\) 上仍是 \(3\)。严格可说的是：

- 没有 \(J\)-一致的正系数下界；
- 当前证明没有给出 \(J\)-独立的 \(c_0\)；
- 不能仅凭四个数值点断言某个统一的“每阶约十倍”衰减律。

---

## 6. Link D：范围及与真实 \(\xi/\xi'\)、Suzuki 的关系

### 6.1 抽象范围

当前引理把 \(a_n>0\)、零点全为 \(\{\pm\gamma_n\}\) 作为抽象假设。证明中没有把 \(\gamma_n\) 识别为 \(\zeta\) 零点，也没有从真实 \(\xi\) 构造 \(A\)。因此作为抽象条件命题，它不循环。

但是，如果日后未经独立证明便令 \(A\) 等于真实 Riemann \(\Xi\) 函数并宣称 (A1) 给出了它的全部零点，那么 (A1) 本身就输入了 RH。故稿件必须保留“不得实例化为真实 \(\xi/\xi'\) 目标”的醒目限制。

### 6.2 \(B=iA'\) 与 (A2)

若 \(A\) 在实轴上为实值且有至少两个相邻实零点，则 Rolle 定理使 \(A'\) 在其间有非零实零点；\(B=iA'\) 有相同零点。因此这种导数耦合与

\[
Z(B)\cap\mathbb R=\{0\}
\]

不相容。该论证是初等的，不需要 RH。原稿对真实导数耦合的排除方向正确，但应明确所用的“实轴实值”条件。

### 6.3 Suzuki entire family

Suzuki 2013, Theorem 2.2(2),(7) 确认其变形族为整函数且固定参数时阶至多为 1。然而“整函数列不能在含目标极点绕圈的穿孔域上紧一致收敛到该亚纯目标”是另一个命题。若收敛是紧开拓扑，取围绕目标简单极点的小圆 \(C\)，则每个整近似的积分为 0，而目标积分为

\[
2\pi i\operatorname{Res}(W;p)\ne0;
\]

圆周上一致收敛会导致矛盾。若指球面收敛、仅点态收敛或随域变化的其他拓扑，则必须另行分析。

OB-35 没有把抽象 \(F^{(c)}\) 重新宣称为 Suzuki 族成员，这一点正确。当前引理不需要上述 Suzuki 事实才能成立。

---

## 7. RH 非循环性审计

| 可能的 RH 输入 | 本证明是否使用 | 说明 |
|---|---|---|
| 所有非平凡 \(\zeta\) 零点在临界线 | 否 | 没有实例化真实 \(\zeta\) 零点 |
| \(\gamma_n\) 为真实零点纵坐标 | 否 | \(\gamma_n\) 只是 (A1) 的抽象参数 |
| RH 等价的正定性、零点实性或谱陈述 | 否 | IFT、插值余项与 Cauchy 估计均为局部解析事实 |
| \(B=iA'\) 的真实目标关系 | 否 | 当前 (A1)–(A3) 明确令 \(A,B\) 独立 |
| Suzuki 的 RH 判据 | 否 | Suzuki 只用于范围说明，不参与推导 |

**Q1 裁决：CONFIRMED，仅限抽象引理。** 一旦把 (A1) 未经证明地施加于真实 \(\Xi\)，非循环性即失效；当前稿件的“不适用于真实目标”限制不可删除。

---

## 8. Links A–D 与 Gate-A 问题逐项回答

### 8.1 Links A–D

| 链节 | 独立裁决 | 理由 |
|---|---|---|
| Link A：jet IFT 基点 | CONFIRMED | \(\Psi(x,0)=0\) |
| Link A：Jacobian | CONFIRMED | 精确式 (2.8) 非零 |
| Link A：尾项可微性 | CONFIRMED | (2.6) 与 \(\sum y_m<\infty\) 给出一致控制 |
| Link A：jet 匹配 | CONFIRMED | (2.9)–(2.11)；匹配索引必须写成 \(0\le j<J\) |
| Link A：记录类成员资格 | CONDITIONAL | 数学上可证，但 \(\mathcal E_N^{\rm mer}\)、normalization 和 \(N\) 尚未精确定义 |
| Link A：\(F^{(c)}\ne W\) | CONFIRMED | 有序尾零点对 \(c<0\) 严格移动 |
| Link B：三次项 | CONFIRMED | 式 (3.4) |
| Link B：\(d=3\iff\Delta_1\ne0\) | CONFIRMED | 式 (3.5) |
| Link B：更高次数 | TEXTUAL ERROR | 应用 (3.6)，不是“next odd \(r\)” |
| Link B：Cauchy 下界 | CONFIRMED | 仅对 \(0<R<R_B\)，并需空集约定 |
| Link C：一般 \(\Delta_1'(0)\ne0\) | NOT PROVED AS WRITTEN / REPAIRED HERE | 四个特例不证明全称命题；(0.1) 给出完整证明 |
| Link C：四个数值锚点 | PARTLY REFUTED | \(J=4\) 锚点错误 |
| Link C：“约 10 倍/degree 非一致” | REFUTED AS WORDED | 实际比值及逻辑结论见 §5 |
| Link D：抽象而非真实 \(\xi/\xi'\) | CONFIRMED | 当前推导未作真实实例化 |
| Link D：Suzuki 范围 | CONDITIONAL | 排除方向正确；应补 Suzuki 2013, Thm. 2.2(2),(7) 并定义收敛拓扑，或删除非承载性陈述 |

### 8.2 Q1–Q5

**Q1 — Non-circularity：** **YES，限抽象范围。** 没有 RH 输入。若用于真实 \(\Xi\)，(A1) 可能就是 RH 输入，故不得越界实例化。

**Q2 — Refined degree：** **YES，附一处文字修正。** 三次项、\(\Delta_1\) 判据和 Cauchy 下界正确；旧 \(z^{2J+3}\) 已正确退出当前 jet 分支。更高项应写为 \(q_0\mapsto2q_0+1\)。

**Q3 — \(\Delta_1'(0)\ne0\) 与非一致性：** **现稿证据 NO；结论经 (0.1) 修复后 YES。** 符号交替对所有 \(J\) 成立。\(J=4\) 数值须改；“约 10 倍”和“degree 不 uniform”须删除。可保留“系数无正的 \(J\)-一致下界、未证明统一 \(c_0\)”的准确表述。

**Q4 — Scope：** **YES，附引用/拓扑修正。** 抽象范围没有重新声称真实 \(\xi/\xi'\) 或 Suzuki 结果。Suzuki 的具体 entire 性应精确引为 2013, Theorem 2.2(2),(7)。

**Q5 — 最终 Gate-A：** **GATE-A CONDITIONAL。** 当前文字不得升级；完成第 9 节全部强制修改后，可升级为抽象 E′-neg 引理，且必须继续标注“不是 Suzuki-target result”。

---

## 9. 必须先完成的确切修改列表

以下修改全部为升档前置条件。

### M1 — 重写记录类定义

把当前一句 `Finite record ℰ_N^{mer}: ...` 全部替换为：

> Define \(\mathcal E_{k,J}^{\rm mer}(w_0)\) to be the class of odd meromorphic functions \(F\) of conventional order at most one such that: (i) the finite poles of \(F\), with multiplicity, are exactly those of \(W\); (ii) the first \(k\) positive real zeros, counted with multiplicity, are the simple zeros \(\gamma_1,\dots,\gamma_k\); (iii) \(\lim_{z\to0}F(z)/z=A(0)/\widetilde B(0)\); and (iv) \(F^{(j)}(w_0)=W^{(j)}(w_0)\) for every integer \(0\le j<J\).

若必须保留下标 \(N\)，则须明确定义 \(N\) 与 \((k,J,w_0)\) 的关系。

### M2 — 补齐构造符号

在 lemma 前插入第 2 节的 (2.1)–(2.5)，特别是 \(A_{u,c}\)、\(F^{(c)}\)、\(x_\ell,y_m,b_m(c)\) 和全部求和范围。明写 \(A,B\) 为整函数。

### M3 — 用一般证明替换“script-verified, exact”作为主证明

删除“由 \(\gamma_n=n,k=1,w_0=i,J=1,\dots,4\) 的数值推出每个固定 \(J\)”这一推理。插入 (0.1) 或等价的 (4.1)–(4.6) 推导，并将小邻域写成

\[
c_0=c_0(A,k,J,\tau)>0.
\]

数值只能保留为 sanity check，不得承载全称命题。

### M4 — 改正数值段

将四个锚点替换为例如

\[
0.03385805626,\quad
-0.001414395659,\quad
4.336708886\times10^{-5},\quad
-9.84706645\times10^{-7}.
\]

将“falls ~10× per unit \(J\)”替换为：

> In this model the successive absolute-value ratios for \(J=1\to4\) are approximately \(23.94,32.61,44.04\); no asymptotic rate is inferred from these four values.

### M5 — 改正非一致性表述

删除

> neither degree nor constant is uniform in \(J\)

并替换为：

> For every fixed \(J\), the local leading degree is \(3\). No \(J\)-independent neighborhood in \(c\) is proved, and the linearized cubic coefficient has no positive lower bound uniform in \(J\); indeed (5.3) tends to zero for fixed \(A,k,\tau\).

### M6 — 改正更高次数句

把

> If \(\Delta_1(c)=0\), the degree is the next odd \(r\) with \(\Delta_r(c)\ne0\).

替换为：

> For \(q\ge1\), define \(\Delta_q(c)\) by (3.1). If \(q_0\) is the least index with \(\Delta_{q_0}(c)\ne0\), then the leading degree is \(2q_0+1\) and its coefficient is \(-A(0)\Delta_{q_0}(c)/(q_0\widetilde B(0))\).

### M7 — 明确 Cauchy 圆盘

保留 \(0<R<R_B\)，并增加：若 \(Z(B)\setminus\{0\}=\varnothing\)，约定 \(R_B=+\infty\)。不得把同一估计无条件延伸到跨过极点的圆。

### M8 — 修复引用与范围段

- 把“OB-09-confirmed core”改成当前稿内的自包含证明，或至少精确指向 `OB-09-E-prime-neg-IFT-odd-meromorphic.md`, §7.1–§7.2, eqs. (7.3)–(7.7)。
- 若保留 Suzuki entire 性，加入 Masatoshi Suzuki (2013), Theorem 2.2(2),(7), DOI 10.4064/aa157-3-1。
- 若保留“no moving-pole convergence”，定义为穿孔域上的 compact-open convergence，并加入 §6.3 的轮廓积分证明；否则删除该非承载性句子。

---

## 10. 最终裁决

### GATE-A CONDITIONAL

1. **数学核心：** 可成立。Link A 的 jet-IFT 构造、Link B 的三次项及 Cauchy 下界均通过独立检查。
2. **关键缺失证明：** 现稿没有证明抽象全量词下的 \(\Delta_1'(0)\ne0\)；但精确公式 (0.1) 补上后，该结论对所有允许数据成立，并给出交替符号。
3. **数值：** \(J=4\) 锚点错误；衰减倍数描述错误。
4. **非循环性：** 抽象范围内通过；不得把 (A1) 未经独立证明地实例化为真实 \(\Xi\) 的全部零点。
5. **范围：** 只能升级为抽象 odd-meromorphic jet non-identifiability lemma；明确不是真实 \(\xi/\xi'\) 或 Suzuki-target 定理。

**升级条件：** 完成 M1–M8 后，可将该抽象引理从 `PROOF-DRAFT` 升为 `INDEPENDENTLY-CHECKED`。在修改前，不予升级。

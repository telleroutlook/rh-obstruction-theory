# OB-34 — `O_finite^{(K)}` 与 `O_theta^{samp}` 不可比性的独立审稿裁决

**审稿日期：** 2026-08-13  
**审稿对象：** `OB-34-H-incomparability-resend.md`  
**最终裁决：** **GATE-A CONDITIONAL**

原稿的不可比性结论有一条可严格完成的修正版，但**原稿目前不能直接标为
INDEPENDENTLY-CHECKED**。见证 1 的结构正确，不过其 `Li_1` 数值与原稿自己的定义相差
因子 `2`；见证 2 的关键推断

\[
2\sum_k n_k+4R\ge 4
\]

不由 `R\ge1` 推出，而且存在满足 B2 全部代数条件、同时使左端**恰好等于零**的精确有理
反例。另有三个陈述层面的必修问题：`\mathfrak X_{\rm sym}` 未排除使 `\phi_j` 无定义的
`0,1`；采样层没有声明为正，因而所谓“非恒定”并非按现有量词成立；B2 被误写成适用于
“任意有限测试族”，且 `OB-20/OB-21` 交叉引用无法按现有文件标识核实。

这些问题可以用第 8 节列出的逐字修改修复。修复后的定理对每个 `K\ge1`、每个非空有限
正采样层集均成立，且完全不使用 RH。

---

## 1. 审稿边界、被引前提与引用核对

本审稿独立检查原稿中的定义、两个见证、量词、方向标签、精确数值和非循环性。没有把
作者的 Gate 状态当作数学前提。

### 1.1 可核实的内部前提

| 原稿所指内容 | 实际核实到的精确来源 | 精确位置与覆盖范围 | 审稿判断 |
|---|---|---|---|
| “Theorem B2，任意有限测试族” | `OB-02-B2-integer-collision.md`，内部文件日期 2026-08-11；文件未列作者 | **Theorem B2**；Lemma 3.1（特定 Li 矩阵可逆）；Lemma 4.1（四元组向量为非零有理向量）；(5.1)–(5.8)（清分母、整数重数、精确碰撞）；§6（对称性与 `R\ge1`） | **只覆盖特定测试族** `\phi_j(\rho)=1-(1-1/\rho)^j`, `j=1,\ldots,m`，不覆盖任意测试函数；对本题的 `O_finite^{(K)}` 足够。 |
| “独立 checker replay” | `OB-13-B2-independent-exact-reconstruction.md`，内部文件日期 2026-08-11；文件未列作者 | Lemma 2.1–2.3；§§3–5 的 `m=2,3` 精确实例；§6 的 `fractions.Fraction` 独立程序与 V1–V5 | **确认显式实例及归一化**；它不是“所有任意测试族”的定理。全 `K` 量词依赖前一文件的 Theorem B2 证明。 |
| “Theorem G 的 `d_n`” | `OB-17-G-diagonal-fredholm-interval-replay.md`，内部文件日期 2026-08-11；文件未列作者 | “Riemann–Siegel theta function and Gram-type levels”：`\theta(d_n)=(n-1)\pi` | 该处的 `d_n` 是由 `\theta` 固定的、与 `\mathcal Z` 无关的数列；文件本身没有把它定义成 `\mathcal Z` 上的观测映射。若另定义 `O_{\rm const}(\mathcal Z):=(d_n)`，该映射才是恒定映射。 |

原稿写的 “Gate-A PASS OB-20 + checker OB-21” 没有给出文件名、版本或稳定定理定位；按
现有材料不能把这两个标签核实为所声称的前提。可核实且假设覆盖本题对象的是上表中的
`OB-02` 与 `OB-13`。正式文本必须改用这些精确标识，或补上 `OB-20/OB-21` 的稳定文件名、
版本、作者、日期及定理号。不得凭空补写作者信息。

### 1.2 外部定理

修正版证明不需要任何外部深定理。所用事实只有有限多重集可加性、初等有理函数运算、
Vandermonde/Chebyshev 计算以及“非零多项式不能在非空开集上恒为零”；最后一个事实在
第 5.3 节内直接给出归约，因而没有未核实的外部作者—年份—定理号输入。

---

## 2. 定义、量词与符号逐项审查

### 2.1 `\mathfrak X_{\rm sym}`

原稿只写“finite zero-multisets symmetric under conjugation and `\rho\mapsto1-\rho`”。这
不足以保证 `\phi_j(\rho)` 与 `\phi_j(1-\rho)`有定义：若多重集含 `0`，反射对称性还会使
它含 `1`，而两个分母均会出问题。

**必须修正为**有限多重集位于开临界带

\[
\{\rho\in\mathbb C:0<\Re\rho<1\},
\]

或至少明确 `\mathcal Z\cap\{0,1\}=\varnothing`。采用开临界带后，两个见证和 B2 对象都
落在该域内，且 B2 的假设完全覆盖。

### 2.2 `O_finite^{(K)}` 与实值性

对修正后的域，

\[
\operatorname{Li}_j(\mathcal Z)
=\sum_{\rho\in\mathcal Z}
 \bigl(\phi_j(\rho)+\phi_j(1-\rho)\bigr)
\]

是有限和，因而良定义。反射映射按重数置换 `\mathcal Z`，所以

\[
\operatorname{Li}_j(\mathcal Z)=2\sum_{\rho\in\mathcal Z}\phi_j(\rho).
\tag{2.1}
\]

共轭对称性与 `\phi_j(\bar\rho)=\overline{\phi_j(\rho)}` 又保证右端为实数。因此
`O_finite^{(K)}:\mathfrak X_{\rm sym}\to\mathbb R^K` 正确，但这是**反射双计数归一化**，
不是普通的逐原子 Li 和。

B2 原文件采用共轭双计数

\[
\sum_{\rho\in\mathcal Z}
  (\phi_j(\rho)+\phi_j(\bar\rho)).
\]

在同时具有共轭与反射对称性的 `\mathcal Z` 上，它也等于
`2\sum_{\rho\in\mathcal Z}\phi_j(\rho)`，故 B2 的归一化确实覆盖本题，未发生隐蔽的
比例错配。

### 2.3 `O_theta^{samp}`

应先固定整数 `M\ge1` 及实数采样层。原稿的“genuine, nonconstant”只有在至少有一个
非负可见层时才可能成立；若所有 `d_m<0`，则

\[
N_{\mathcal Z}(d_m)=0
\]

对每个 `\mathcal Z` 都成立，观测是恒定的，不可能与任意非恒定观测不可比。为与后面的
B2 正高度构造无缝相容，最清楚的定理量词是

\[
M\ge1,\qquad 0<d_1<\cdots<d_M.
\tag{2.2}
\]

在 (2.2) 下，该映射确实非恒定：取两个临界线共轭对，一个高度小于 `d_1`，另一个高度
大于 `d_M`，它们的第一个计数坐标不同。

### 2.4 `O_oracle`、预序与严格符号

`O_oracle(\mathcal Z)=\mathcal Z` 正确；对任意观测 `O`，都有
`O\preceq O_oracle`。所给 `\preceq` 是预序而非多重集上的反对称偏序；原稿没有宣称格，
这一点正确。

原稿使用了未定义的 `\not\preceq` 风格符号 `⋠` 和严格符号 `\prec`。建议一律写成
`O_a\npreceq O_b`，并把“恒定观测严格较粗”展开为

\[
O_{\rm const}\preceq O_finite^{(K)},
\qquad
O_finite^{(K)}\npreceq O_{\rm const}.
\]

---

## 3. 见证 1：同高度四元组

令

\[
\mathcal Z_a=Q(3/4,10),\qquad
\mathcal Z_b=Q(9/10,10).
\]

两者的虚部多重集均为 `\{-10,-10,10,10\}`，故对每个实数 `u` 都有

\[
N_{\mathcal Z_a}(u)=N_{\mathcal Z_b}(u).
\]

所以它们在任意固定采样层集上的 `O_theta^{samp}` 完全相同。这一链节**确认**。

但原稿给出的两个分数是普通逐原子和

\[
S(\sigma,T):=\sum_{\rho\in Q(\sigma,T)}\frac1\rho
=\frac{2\sigma}{\sigma^2+T^2}
 +\frac{2(1-\sigma)}{(1-\sigma)^2+T^2},
\]

而按原稿 (2.1) 的定义，`\operatorname{Li}_1(Q)=2S(\sigma,T)`。使用 Python 标准库
`fractions.Fraction` 的精确有理运算得到

\[
\begin{aligned}
S(3/4,10)&=\frac{51296}{2576009},\\
S(9/10,10)&=\frac{2001800}{100820081},\\
\operatorname{Li}_1(\mathcal Z_a)
 &=\frac{102592}{2576009}
 \approx0.0398259478131,\\
\operatorname{Li}_1(\mathcal Z_b)
 &=\frac{4003600}{100820081}
 \approx0.0397103430218,
\end{aligned}
\]

且精确差为

\[
\operatorname{Li}_1(\mathcal Z_a)-
\operatorname{Li}_1(\mathcal Z_b)
=\frac{30024117552}{259713436036729}>0.
\tag{3.1}
\]

因此见证 1 的**逻辑结论正确**，但数值锚点必须整体乘 `2`，或者全篇改用普通逐原子和并
同步调整 B2 归一化。保留现定义并改数值是较小修改。

该见证给出

\[
O_finite^{(K)}\npreceq O_theta^{samp}
\qquad(K\ge1),
\]

方向标签正确，因为右侧观测碰撞而左侧观测不碰撞。

---

## 4. B2 碰撞前提的精确适用范围

固定 `K\ge1`。Theorem B2 实际证明的是：可任选互异正有理数
`t_1<\cdots<t_K` 及正有理数 `T`，令 `C` 为前 `K` 个特定 Li 测试在临界线对上的贡献
矩阵，令 `q(T)` 为 `Q(3/4,T)` 的贡献向量；则 `C` 可逆，

\[
\beta=-C^{-1}q(T)\in\mathbb Q^K.
\]

取正整数 `R` 清除 `\beta` 的分母并令 `n=R\beta\in\mathbb Z^K`，再取
`M_0=\max_k|n_k|`，就有合法的非负重数及精确恒等式

\[
Cn+Rq(T)=0.
\tag{4.1}
\]

于是碰撞只对

\[
j=1,\ldots,K
\]

成立。原稿中“equal for all `j`”若被理解成所有正整数 `j`，是错误的；必须改为
“equal for all `j=1,\ldots,K`”。对每个给定 `K` 重新构造一对见证，足以证明“对每个
`K`”的定理。

`R\ge1` 确实成立，因为 `R` 是正的分母公倍数；`M_0+n_k\ge0` 由缓冲定义成立。
`T>t_K` 不是 B2 所必需的假设，但 B2 允许自由选择有理参数，故可额外安排该不等式。

---

## 5. 见证 2：原证明的确切间隙与可证明修复

### 5.1 两个计数公式

若 `t_K<T`，则对 `u\in(t_K,T)`，全部临界线对已计入而四元组尚未计入，故

\[
N_{\mathcal Z_-}(u)-N_{\mathcal Z_+}(u)
=2\sum_{k=1}^K n_k.
\tag{5.1}
\]

对 `u\ge T`，因定义使用 `\le u`，四元组也已计入，故

\[
N_{\mathcal Z_-}(u)-N_{\mathcal Z_+}(u)
=2\sum_{k=1}^K n_k+4R.
\tag{5.2}
\]

这两个等式均确认。问题在于原稿随后把 (5.2) 宣称为 `\ge4`。`n_k` 是有符号整数，B2
只保证 `M_0+n_k\ge0`，完全没有给出 `\sum n_k\ge0`。

### 5.2 载荷性断言的精确反例

以下数据全部为有理数，并满足 `0<t_1<t_2<T`：

\[
K=2,qquad
t_1=\frac1{24},\qquad
t_2=\frac9{40},\qquad
T=\frac38,qquad \sigma_0=\frac34.
\]

从 `\phi_j` 定义直接用 `Fraction` 精确重算得到

\[
C=
\begin{pmatrix}
1152/145&3200/481\\
4608/21025&1036800/231361
\end{pmatrix},
\qquad
q(T)=
\begin{pmatrix}
1792/195\\95232/4225
\end{pmatrix},
\]

并且

\[
\det C=\frac{6643777536}{194574601}>0.
\]

以及

\[
\beta=-C^{-1}q(T)
=\left(\frac{841}{264},-\frac{1369}{264}\right).
\]

取

\[
R=264,qquad n=(841,-1369),qquad \sum_kn_k=-528,
\]

则精确余量为

\[
Cn+Rq(T)=(0,0)^T,
\]

但

\[
2\sum_kn_k+4R=-1056+1056=0.
\tag{5.3}
\]

所以在 `u=T` 或任意 `u>T`，这对 B2 多重集的采样计数**完全相同**。这不仅否定
“`\ge4`”，还证明四元组的四个原子可以被临界线重数变化精确抵消。原稿的“either way”
因此是实质性证明间隙，而不是符号方向的小笔误。

### 5.3 保留单个正采样层的非消去修复

该间隙可用下述初等参数选择引理修复，而无需 RH，也无需改变 B2 的碰撞构造。

> **非消去参数选择引理。** 固定 `K\ge1` 与 `d_*>0`。可以选择有理数
> \[
> 0<t_1<\cdots<t_K<T<d_*
> \]
> 使 B2 向量 `\beta=-C^{-1}q(T)` 满足
> \[
> G_K(t_1,\ldots,t_K,T):=2+\sum_{k=1}^K\beta_k\ne0.
> \tag{5.4}
> \]

**证明。** 在 `0<t_1<\cdots<t_K<T` 上，B2 的行列式公式保证 `C` 可逆。对固定 `K`，
`C`、`q(T)`、`\beta` 与 `G_K` 都是参数的实有理函数。固定任意互异正 `t_k` 并令
`T\to\infty`；由

\[
\phi_j(a+iT)=1-\left(1-\frac1{a+iT}\right)^j\longrightarrow0
\]

可知 `q(T)\to0`，从而 `\beta\to0`、`G_K\to2`。故 `G_K` 不是恒零有理函数。

若它在非空开集

\[
U_{d_*}=\{0<t_1<\cdots<t_K<T<d_*\}
\]

上恒为零，清除分母后所得分子多项式就在开集上恒为零；逐变量把它看成一元多项式，即得
所有系数多项式均为零，故该分子是零多项式。这与 `T\to\infty` 时 `G_K\to2` 矛盾。
因此 `U_{d_*}` 中有 `G_K\ne0` 的点；非零性是开条件，而有理点在该开集稠密，故可把
全部参数选成有理数。证毕。

现在取任一固定正采样层，例如 `d_*=d_1`，按引理选择参数。清分母后
`n_k=R\beta_k`。由于所有临界线对和四元组都位于 `d_*` 以下，

\[
\begin{aligned}
N_{\mathcal Z_-}(d_*)-N_{\mathcal Z_+}(d_*)
 &=2\sum_kn_k+4R\\
 &=2R\left(\sum_k\beta_k+2\right)\\
 &=2R\,G_K\ne0.
\end{aligned}
\tag{5.5}
\]

与此同时，(4.1) 给出

\[
O_finite^{(K)}(\mathcal Z_-)
=O_finite^{(K)}(\mathcal Z_+)
\]

的精确等式。因此修复后的见证 2 给出

\[
O_theta^{samp}\npreceq O_finite^{(K)}.
\]

方向标签正确。注意此修复证明的是“存在一个避免计数消去的 B2 参数点”，而不是错误地
声称每个 B2 参数点都自动分离采样计数。

---

## 6. 非循环性审查

修正后的完整证明通过以下检查：

1. 两个见证都是人工构造的有限多重集；没有把它们认作 `\zeta` 或任何 `L`-函数的零点。
2. B2 只使用 Chebyshev/Vandermonde、有理线性代数和整数清分母。
3. 没有使用任何 `\zeta` 零点纵坐标 `\gamma_n`，也没有使用“所有零点在临界线”或其
   等价命题。
4. `P(\mathcal Z_+)=1` 只是人工多重集的有限几何性质；见证 2 的不可比性证明甚至不需
   使用谓词 `P`。
5. 固定的 `d_n`/采样层若来自 `\theta`，只作为预先给定的正实数；不读取零点位置。
6. 非消去引理只排除一个有理函数的零集合，不含 RH、显式公式或零点实性输入。

**结论：** 没有 RH 输入，也没有 RH 等价命题输入；非循环性确认。

---

## 7. Gate-A 问题逐项回答

| 问题 | 独立判断 |
|---|---|
| **Q1 非循环性** | **确认。** B2 及修复后的参数选择完全是有限代数；没有 RH 或实际零点输入。 |
| **Q2 映射良定义** | **原文不完全确认。** 必须排除 `0,1`，声明 `M\ge1` 且采样层为正。修正后 `O_theta^{samp}` 非恒定，`O_oracle=\mathcal Z` 正确。Theorem G 只提供固定 `d_n`；只有把该固定序列包装成 `\mathcal Z` 上的映射后，才可称恒定观测。 |
| **Q3 见证 1** | **结构确认、数值否定后修正。** 同虚部计数完全相同；按现定义正确的 `Li_1` 分数是原稿的两倍，见 (3.1)。方向标签正确。 |
| **Q4 见证 2** | **原证明否定。** B2 的前 `K` 个 Li 碰撞、`R\ge1`、两个计数公式均确认；“`2\sum n_k+4R\ge4`”及“either way”被精确反例 (5.3) 否定。加入非消去参数选择引理后，该方向成立。只能写 `j=1,\ldots,K`，不能写无穷全称“all `j`”。 |
| **Q5 范围/诚实性** | `O_theta^{samp}` 与固定常量序列的区分、预序而非格的定位均可保留。原稿“没有新待审构造”目前不准确，因为采样分离尚缺非消去选择；加入并证明第 5.3 节引理后，可准确说“除 B2 外只新增一个初等参数避免引理，不增加解析数论内容”。H 仍只是信息预序的组织框架，不是独立 barrier。 |
| **Q6 Gate-A** | **GATE-A CONDITIONAL。** 完成第 8 节全部必修文字修改后，可把修正版 H'(i) 升为 INDEPENDENTLY-CHECKED；修改前不得升级。 |

---

## 8. 必须先完成的确切文字修改

以下修改是本裁决从 CONDITIONAL 转为 PASS 的充分且必要文本修复集。

### M1 — 替换对象域与采样量词

把定义段开头替换为：

> Fix integers `K\ge1` and `M\ge1`, and fix real sampling levels
> `0<d_1<\cdots<d_M`. Let `\mathfrak X_{\rm sym}` be the class of finite multisets
> contained in `{\rho\in\mathbb C:0<\Re\rho<1}`, invariant with multiplicity under
> `\rho\mapsto\bar\rho` and `\rho\mapsto1-\rho`.

### M2 — 明确 `Li_j` 的双计数归一化

把“for `j=1`, `Li_1=\sum1/\rho` up to the reflection”替换为：

> Because `\mathcal Z` is reflection-symmetric,
> `Li_j(\mathcal Z)=2\sum_{\rho\in\mathcal Z}\phi_j(\rho)`; in particular
> `Li_1(\mathcal Z)=2\sum_{\rho\in\mathcal Z}1/\rho`. Conjugation symmetry makes
> these values real.

### M3 — 改正 B2 的引用与适用范围

把“for any finite test family”及 `OB-20/OB-21` 句替换为：

> For every `m\ge1`, Theorem B2 in `OB-02-B2-integer-collision.md`, Theorem B2,
> Lemmas 3.1 and 4.1 and equations (5.1)–(5.8), constructs an exact collision for
> the specific Li family `\phi_j`, `j=1,\ldots,m`. Its normalization agrees with the
> present one on `\mathfrak X_{\rm sym}`. The independent exact replay
> `OB-13-B2-independent-exact-reconstruction.md`, Lemmas 2.1–2.3 and V1–V5,
> checks the normalization and the explicit `m=2,3` instances. No claim is made
> here for an arbitrary finite family of unrelated test functions.

并把 `\sigma_0\in(1/2,1)` 收窄为已核实的 `\sigma_0=3/4`；若要保留一般 `\sigma_0`，必须
另给一般化定理及其精确证明定位。

### M4 — 改正见证 1 的所有数值锚点

把两处分数和小数统一替换为：

> `Li_1(Q(3/4,10))=102592/2576009=0.039825947813\ldots`, whereas
> `Li_1(Q(9/10,10))=4003600/100820081=0.039710343022\ldots`.

可在括号中说明原来的两个分数是未乘反射因子 `2` 的普通逐原子和。

### M5 — 改正有限量词

把见证 2 中两处“equal for all `j`”及“exact, all `j`”替换为：

> equal exactly for every `j=1,\ldots,K` (with a new B2 pair chosen for each fixed
> `K`).

### M6 — 整段删除错误的自动分离论证

删除以下三类句子：

> choose ... some `d_m\in(t_n,T]`;  
> a level just above `T` gives `2\sum n_k+4R\ge4`;  
> either way the sampled counts differ.

用第 5.3 节“非消去参数选择引理”及 (5.5) 的证明逐字等价地替换。载荷性结论必须写成
“**可以选择**参数使 `G_K\ne0`”，不能写成“任意 B2 对都由四元组自动分离”。

### M7 — 改正 Theorem G/恒定观测的表述

把“Theorem G's literal `d_n=theta_level(n)` is constant”替换为：

> The levels `d_n` defined from `\theta` in Theorem G are fixed and
> `\mathcal Z`-independent. If one defines the observation
> `O_const(\mathcal Z):=(d_n)`, then `O_const` is constant and hence strictly
> coarser than the nonconstant `O_finite^{(K)}`. This constant map is not
> `O_theta^{samp}`.

### M8 — 改正最终范围声明

最终定理应写为：

> **Corrected Theorem H'(i).** Fix `M\ge1` and positive levels
> `0<d_1<\cdots<d_M`. On the corrected class `\mathfrak X_{\rm sym}`, for every
> `K\ge1`,
> `O_finite^{(K)}\bowtie O_theta^{samp}`. The first non-refinement is witnessed by
> the same-height quartets; the reverse non-refinement is witnessed by a B2 pair
> selected using the non-cancellation lemma above. This is an RH-free statement
> about finite artificial multisets and an information-refinement preorder, not a
> standalone analytic barrier.

---

## 9. 最终裁决

**GATE-A CONDITIONAL。**

可以确认的核心是：同高度四元组确实否定一个细化方向；B2 确实为每个固定 `K` 提供前
`K` 个 Li 型观测的精确碰撞；通过一个明确、已在本文证明的非消去参数选择，可以使该
碰撞在任一预定正采样层上产生不同计数。因此，**修正版不可比性定理为真且非循环**。

不能确认的是原稿当前的载荷性句子、当前数值归一化和当前无条件采样量词。尤其是精确
反例 (5.3) 排除了把 `R\ge1` 当成“新增四元组必然使总计数至少增加 4”的理由。

在 M1–M8 全部落稿后，H'(i) 可由 PROOF-DRAFT 升为 **INDEPENDENTLY-CHECKED**，并应
继续标注：H 是 refinement-preorder 的组织框架，不是独立的 RH barrier。

# OB-39-B 独立审稿裁决

**对象：** *Karamata Tauberian theorem for log-varying counting functions*  
**审稿日期：** 2026-08-14  
**审稿性质：** 数学独立审阅 / Gate-A

## 0. 裁决摘要

- **核心数学蕴含：CONFIRMED。** 若
  \[
  N(\Lambda)\sim C\Lambda\log\Lambda\qquad(C>0),
  \]
  则
  \[
  Z(t)=\int_{[0,\infty)}e^{-tx}\,dN(x)
  \sim C\,t^{-1}\log(1/t),\qquad t\downarrow0.
  \]
- **准确引用：** Bingham–Goldie–Teugels（BGT）, *Regular Variation*（1987），
  **§1.7.2, Theorem 1.7.1, p. 37**。该定理本身就含任意慢变因子；送审件把它描述为
  “只覆盖纯幂”的版本是错误的。
- **ζ 零点应用：CONFIRMED。** Titchmarsh（第二版由 D. R. Heath-Brown 修订，1986）
  Theorem 9.4 的无条件 Riemann–von Mangoldt 公式给出所需计数律；不使用 RH。
- **原稿不能原样通过。** “由 \(\gamma_n\ge14\) 得到几何级数上界”是错误推理，所写上界本身也与
  目标渐近不相容；固定 50 项的数值锚点亦计算错误且原则上不可能检验无限和的 \(t\downarrow0\)
  渐近。

**最终裁决：`GATE-A CONDITIONAL`。** 完成第 8 节列出的确切文字修改后，可改判
`GATE-A PASS / INDEPENDENTLY-CHECKED`。不存在 RH 循环，也不存在无法修复的数学缺口。

---

## 1. 精确对象与量词核对

对 ζ 的应用，必须把序列精确定义为：遍历所有非平凡零点
\(\rho=\beta+i\gamma\)（\(0<\beta<1,\ \gamma>0\)），每个零点按其解析重数计数，并把其
正纵坐标 \(\gamma\) 放入序列；若不同零点具有相同纵坐标，该纵坐标也要重复。这样
\[
N_\zeta(T)=\#\{\rho:\ 0<\Re\rho<1,\ 0<\Im\rho\le T\}
\]
才与 Riemann–von Mangoldt 公式中的计数函数完全一致。若只数“不同的纵坐标”，则现有前提不足以
直接推出同一渐近。

送审件把慢变函数定义为在整个 \((0,\infty)\) 上取正值，却随后以 \(L(x)=\log x\) 为例；后者在
\((0,1]\) 上并不为正。标准定义只要求在无穷远处最终为正。也可规定
\(L(x)=\log x\)（\(x\ge e\)）并在 \((0,e)\) 上作任意正延拓。这是定义域措辞问题，不影响渐近结论，
但应修订。

---

## 2. 引用核验

### 2.1 BGT 的准确结果

BGT 第 1 章的官方目录把 **§1.7.2 “Karamata's Tauberian Theorem”** 定位在印刷页 37；其中的
结果编号为 **Theorem 1.7.1**。按本题所需的归一化，其陈述为：设 \(U\) 非降、右连续，
\(U(x)=0\)（\(x<0\)），且其 Laplace–Stieltjes 变换
\[
\widehat U(s)=\int_{[0,\infty)}e^{-sx}\,dU(x)
\]
对每个 \(s>0\) 有限。若 \(\rho\ge0\)、\(c>0\)，且 \(\ell\) 在无穷远处慢变，则
\[
U(x)\sim \frac{c}{\Gamma(1+\rho)}x^\rho\ell(x)
\quad\Longleftrightarrow\quad
\widehat U(s)\sim c\,s^{-\rho}\ell(1/s).
\]

因此取
\[
U=N,\qquad \rho=1,\qquad c=C,\qquad \ell(x)=\log x
\]
（在小 \(x\) 处作正延拓），并用 \(\Gamma(2)=1\)，立即得到
\[
N(x)\sim Cx\log x
\quad\Longleftrightarrow\quad
Z(t)\sim Ct^{-1}\log(1/t).
\]

故本题不需要 BGT Theorem 1.7.4，也不存在所谓“从纯幂版扩张到对数慢变版”的文献缺口。
原来的“BGT §1.7”方向上没有错，但应精确为“BGT, §1.7.2, Theorem 1.7.1, p. 37”。

可核对来源：

- [BGT 第 1 章官方页面与 DOI](https://www.cambridge.org/core/books/regular-variation/karamata-theory/3AE606B1554DD31F5211C1FFE0F0B3C7)
- [BGT 官方目录（§1.7.2 位于 p. 37）](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/92ABC242FEBEDE566EA28EA26351D63B/9780511721434toc_pvii-xvi_CBO.pdf/contents.pdf)
- [Herdegen–Liang–Shelley, Theorem 3.1：正测度版本及两方向说明](https://arxiv.org/pdf/2205.13075)
- [引用 BGT Theorem 1.7.1 并完整重述慢变因子版本的 Theorem A](https://arxiv.org/pdf/1104.1027)

### 2.2 Titchmarsh–Heath-Brown 的计数律

Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., revised by
D. R. Heath-Brown（1986），**Theorem 9.4** 给出（零点按重数计）
\[
N_\zeta(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+O(\log T).
\]
所以无条件地
\[
N_\zeta(T)\sim \frac{1}{2\pi}T\log T,
\qquad N_\zeta(T)=O(T\log T).
\]
现代文献对该定理编号和公式的逐字形态亦有直接交叉引用，例如
[Garunkštis–Laurinčikas, 式 (1)](https://arxiv.org/pdf/1608.08493)。

---

## 3. BGT 假设逐项核对

| 项目 | 判定 | 独立理由 |
|---|---|---|
| \(N\) 非降、右连续 | PASS | 由 \(N(T)=\#\{\gamma_n\le T\}\) 的定义成立。 |
| 局部有限性 | PASS | ζ 为亚纯函数；非平凡零点在紧子集中离散且有限，重数有限。 |
| 正测度 | PASS | \(dN=\sum_n\delta_{\gamma_n}\ge0\)。 |
| 正则变动指数 | PASS | \(N(T)\sim CT\log T\)，故指数为 \(1\)，慢变因子为 \(\log T\)。 |
| \(Z(t)<\infty\), \(t>0\) | **事实 PASS；原证明 REFUTED** | 由 \(N(T)=O(T\log T)\) 可证；仅由 \(\gamma_n\ge14\) 不能推出。 |
| 常数 | PASS | \(C=1/(2\pi)\)，且 \(\Gamma(2)=1\)，无额外 Gamma 因子。 |
| 所需方向 | PASS | \(N\to Z\) 是 BGT 等价命题的 Abelian 方向。 |
| RH 非循环性 | PASS | 计数所有临界带零点，只使用无条件 Riemann–von Mangoldt 公式。 |

### 原收敛上界为何错误

从 \(\gamma_n\ge14\) 只能知道每一项不超过 \(e^{-14t}\)，完全不能控制有多少项落在各高度区间。
不等式
\[
Z(t)\le \frac{e^{-14t}}{1-e^{-t}}
\]
实际上隐含了类似 \(\gamma_n\ge14+n-1\) 的全局间距条件，而 ζ 零点并无此条件。更直接地，若该上界
对所有小 \(t\) 成立，则右端为 \(O(t^{-1})\)；但已确认的真实渐近为
\(Z(t)\sim (2\pi)^{-1}t^{-1}\log(1/t)\)，二者在 \(t\downarrow0\) 时矛盾。

正确的先验收敛证明为
\[
\begin{aligned}
Z(t)
&=\sum_{k=0}^{\infty}\sum_{k\le\gamma_n<k+1}e^{-t\gamma_n}\\
&\le \sum_{k=0}^{\infty}e^{-tk}N(k+1)
\ll \sum_{k=0}^{\infty}e^{-tk}(k+1)\log(k+2)<\infty.
\end{aligned}
\]

---

## 4. 不依赖 BGT 的 Abelian 证明

这也独立关闭送审件 Step 1。

由上一节先知 \(Z(t)<\infty\)。对截断 Stieltjes 积分分部积分，并令截断端点趋于无穷；因为
\(N(x)=O(x\log x)\) 且 \(e^{-tx}N(x)\to0\)，得到
\[
Z(t)=t\int_0^\infty e^{-tx}N(x)\,dx
=\int_0^\infty e^{-u}N(u/t)\,du. \tag{4.1}
\]

令 \(a_t=\log(1/t)\)。取 \(A\ge e\) 与 \(K>0\)，使得
\(N(x)\le Kx\log x\) 对 \(x\ge A\) 成立，并令 \(M=N(A)\)。当
\(0<t\le e^{-1}\) 时：

- 若 \(u/t<A\)，则
  \[
  \frac{N(u/t)}{t^{-1}a_t}\le \frac{Mt}{a_t}\le M.
  \]
- 若 \(u/t\ge A\) 且 \(0<u\le1\)，则 \(\log(u/t)\le a_t\)，故该比值不超过 \(Ku\)。
- 若 \(u\ge1\)，则 \(\log(u/t)=a_t+\log u\)，故该比值不超过
  \(Ku(1+\log u)\)。

因此对所有 \(u>0\)，
\[
0\le e^{-u}\frac{N(u/t)}{t^{-1}a_t}
\le e^{-u}\bigl[M+Ku(1+\log_+u)\bigr], \tag{4.2}
\]
而右端在 \((0,\infty)\) 可积。另一方面，对每个固定 \(u>0\)，
\[
\frac{N(u/t)}{t^{-1}a_t}
=\frac{N(u/t)}{C(u/t)\log(u/t)}\,Cu\,
  \frac{a_t+\log u}{a_t}
\longrightarrow Cu. \tag{4.3}
\]
由 (4.1)–(4.3) 和支配收敛定理，
\[
\frac{Z(t)}{t^{-1}\log(1/t)}
\longrightarrow C\int_0^\infty e^{-u}u\,du=C.
\]

送审件列出的另一个积分也正确：
\[
\int_0^\infty e^{-u}u\log u\,du
=\Gamma'(2)=1-\gamma_{\rm EM}.
\]
它乘以 \(t^{-1}\) 后，相对于 \(t^{-1}\log(1/t)\) 的比值趋于零。不过，仅由
\(N(x)\sim Cx\log x\) 不能把 \(C(1-\gamma_{\rm EM})t^{-1}\) 宣称为真实的第二渐近项；未知余项
只受控为 \(o(t^{-1}\log(1/t))\)，可能大于 \(t^{-1}\)。原文应只把该积分用于说明模型主项中的
\(\log u\) 部分是低阶项。

---

## 5. 方向性判断

- \(N\to Z\) 是 **Abelian 方向**；第 4 节的直接证明不需要额外 Tauberian 条件。
- \(Z\to N\) 是较难的 **Tauberian 方向**；BGT Theorem 1.7.1 用 \(N\) 的非降性完成该方向。
- Paper B 只需前一个方向。因此，即使不引用完整等价定理，第 4 节也已充分关闭论文所需链节；但
  BGT Theorem 1.7.1 确实同时覆盖该方向和慢变因子。

---

## 6. ζ 专门化及非循环性

代入 \(C=1/(2\pi)\) 得
\[
Z_\zeta(t)=\sum_{\rho:\,\Im\rho>0}e^{-t\Im\rho}
\sim \frac{1}{2\pi}t^{-1}\log(1/t).
\]
此处和式按零点解析重数计。证明没有使用 \(\beta=1/2\)，也没有使用任何与 RH 等价的命题。
“纵坐标 \(\gamma\) 是实数”只是复数 \(\rho=\beta+i\gamma\) 的定义，不是零点位于临界线的假设。

前 50 个已验证零点的数据只用于有限数值检查，不参与证明，也不把对有限高度的计算验证外推成 RH。

---

## 7. 数值锚点独立复算

采用 Andrew Odlyzko 公布的前 100,000 个零点表的前 50 行（原表声称误差不超过
\(3\times10^{-9}\)），直接计算得到：

| \(t\) | \(Z_{50}(t)\) | \(tZ_{50}(t)\) | \(R(t)=tZ_{50}(t)/\log(1/t)\) |
|---:|---:|---:|---:|
| 0.010 | 22.236179269 | 0.222361793 | 0.048285250 |
| 0.005 | 32.794833035 | 0.163974165 | 0.030948347 |
| 0.001 | 45.834795079 | 0.045834795 | 0.006635266 |

参照值为 \(1/(2\pi)=0.159154943\)。数据来源：
[Odlyzko 零点表主页](https://www-users.cse.umn.edu/~odlyzko/zeta_tables/index.html) 与
[前 100,000 个零点的纯文本表](https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1)。

因此送审件的“\(Z_{50}(0.01)\approx30\text{--}35\)”不准确；更关键的是，其
“\(R(0.01)\approx30/\log100\approx6.5\)”漏乘了定义中的 \(t=0.01\)。

固定 \(K\) 时，
\[
Z_K(t)\longrightarrow K,
\qquad \frac{tZ_K(t)}{\log(1/t)}\longrightarrow0
\quad(t\downarrow0),
\]
故固定 50 项不仅是“收敛很慢”，而是原则上不可能呈现无限和的目标极限。若要作有意义的数值检验，
必须令截断高度 \(T=T(t)\) 随 \(t\downarrow0\) 增长，并控制尾项；例如要求
\(tT(t)\to\infty\)，再取 \(K(t)=N_\zeta(T(t))\)。

---

## 8. Gate-A 问题与必须修改的确切文本

### 8.1 链节判定

1. **Riemann–von Mangoldt \(\Rightarrow N_\zeta\sim(2\pi)^{-1}T\log T\)：PASS。**
2. **计数律 \(\Rightarrow Z(t)<\infty\)：结论 PASS；原给出的几何级数理由 REFUTED。**
3. **Stieltjes 分部积分：PASS，前提由修正后的收敛证明提供。**
4. **支配收敛：PASS，使用 (4.2) 的显式支配函数。**
5. **常数与 Gamma 因子：PASS。** \(\Gamma(2)=1\)。
6. **BGT 引用：核心引用 PASS，但原稿对定理内容的描述 REFUTED。**
7. **有限数值锚点：REFUTED；且与解析证明必须明确分离。**
8. **非循环性：PASS。** 无 RH 输入。

### 8.2 通过前必须完成的文字修改

**修改 M1（零点序列）。** 在 ζ 专门化处加入：

> 序列遍历所有 \(0<\Re\rho<1,\ \Im\rho>0\) 的非平凡零点，每个零点按解析重数计；
> 不同零点若有相同纵坐标，该纵坐标重复出现。

**修改 M2（慢变函数定义）。** 把“\(L:(0,\infty)\to(0,\infty)\) 为正”改为“\(L\) 在
无穷远处最终为正”；或明确 \(\log x\) 只在 \(x\ge e\) 使用并作正延拓。

**修改 M3（BGT 陈述与引用）。** 删除“BGT Theorem 1.7.1 只覆盖纯幂”和“需寻找伴随扩张”两段，
替换为：

> BGT, §1.7.2, Theorem 1.7.1, p. 37 的 Karamata Tauberian theorem 已包含慢变因子：
> 对非降右连续 \(U\)，
> \(U(x)\sim c x^\rho\ell(x)/\Gamma(1+\rho)\) 当且仅当
> \(\widehat U(s)\sim c s^{-\rho}\ell(1/s)\)。取
> \(\rho=1\)、\(c=C\)、\(\ell(x)=\log x\)，即得所需结论。

**修改 M4（\(Z(t)\) 收敛）。** 删除
\[
Z(t)\le e^{-14t}/(1-e^{-t})
\]
及其理由，替换为第 3 节的分块估计
\[
Z(t)\le\sum_{k\ge0}e^{-tk}N(k+1)<\infty.
\]

**修改 M5（DCT）。** 在 Step 1 中加入 (4.2) 的支配函数，并把结论写为
\[
Z(t)=Ct^{-1}\log(1/t)+o\!\bigl(t^{-1}\log(1/t)\bigr).
\]
如保留 \(\Gamma'(2)\) 的计算，必须注明它不构成未经额外余项假设支持的第二阶渐近。

**修改 M6（数值锚点）。** 用第 7 节的表替换原数值，并删除“固定 \(Z_{50}\) 的
\(tZ_{50}\) 像 \(\log(1/t)\) 增长”的说法。明确固定 \(K\) 时 \(R_K(t)\to0\)，该检查只验证代码与
有限数据，不能验证目标渐近。

---

## 9. 最终裁决

### `GATE-A CONDITIONAL`

数学主命题以及 Paper B 实际需要的方向均已独立确认；BGT 的准确引用也已定位。阻止原稿直接
PASS 的不是主定理缺失，而是三类可精确修复的陈述错误：

1. 对 BGT Theorem 1.7.1 覆盖范围的错误描述；
2. 从 \(\gamma_n\ge14\) 推导收敛的错误上界；
3. 固定 50 项数值锚点的漏因子、错误数值及错误极限解释。

完成 M1–M6 后，整条链
\[
\text{无条件 Riemann--von Mangoldt}
\Longrightarrow N_\zeta(T)\sim(2\pi)^{-1}T\log T
\Longrightarrow Z_\zeta(t)\sim(2\pi)^{-1}t^{-1}\log(1/t)
\]
无缺口、无循环，可推进为 `GATE-A PASS`。

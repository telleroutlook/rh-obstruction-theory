# OB-37 独立审稿裁决：B-form boundedness

**送审件：** OB-37-B-form-boundedness.md  
**审稿类型：** 数学独立审阅 / Gate-A  
**日期：** 2026-08-14  
**最终裁决：** **GATE-A CONDITIONAL**

## 0. 结论摘要

核心数学结论是正确的：若 \(P\) 是闭流形上正的、自伴的、\(m>0\) 阶椭圆伪微分算子，而对称扰动 \(Q\) 属于某个严格低于 \(m\) 的标准 Hörmander 类 \(\Psi^r_{1,0}(M)\)，则 \(Q\) 对 \(P\) 的闭二次型具有相对界 \(0\)。特别地，若

\[
Q\in\bigcap_{0<\varepsilon<1}\Psi^{m-1+\varepsilon}_{1,0}(M),
\]

则对每个 \(\delta>0\) 都存在有限的 \(C_\delta\)，使

\[
|q_Q[u]|\le \delta q_P[u]+C_\delta\|u\|^2,
\qquad u\in H^{m/2}(M).
\]

但是，送审稿**不能原样判为 CONFIRMED / GATE-A PASS**。至少有以下实质性错误或未闭合点：

1. Step 2 声称对任意 \(m>0\)、任意 \(0<\varepsilon<1\)，都有 \(0<m-1+\varepsilon<m\)。这是假的。
2. “\(m\le1\)”特例在 \(m=1\) 处错误；此时 \(m-1+\varepsilon=\varepsilon>0\)，不能据此断言 \(Q\) 为 \(L^2\)-有界。
3. 按通常的严格定义，\(\Psi_{\rm cl}^{m-1+\varepsilon}\) 不是适合这里的过滤符号类；送审稿的圆周锚点 \(i\,d/dx\) 一般并不属于 \(\Psi_{\rm cl}^{1+\varepsilon}\)。对数多齐次符号应写入普通 \(\Psi^{m-1+\varepsilon}_{1,0}\) 类，或另行精确定义对数多齐次类。
4. “上述交集等价于任意严格低阶”不成立；交集条件比“存在某个严格低于 \(m\) 的阶”更强。
5. \(u\in H^{m/2}\) 时，\(\langle Qu,u\rangle\) 未必是字面上的 \(L^2\) 内积；须明确定义为 Sobolev 对偶配对并由稠密性延拓。
6. Step 3 的强制性 Gårding 估计正确，但 \(C_1'\) 一般依赖 \(P\) 的有限个完整符号半范数（包括主符号导数），不能声称只依赖低阶项。
7. 数值锚点给出的 \(1/(4\delta)\) 是有效常数，却不是所声称的最优常数；连续极值中还漏掉了 \(-\delta\)，最后的平方恒等式漏掉了 \(+\delta\)。
8. 多处书目没有标题、版本、页码或精确定理号；其中 Shubin “Thm 2.2 / Thm 3.3”及 Taylor “Thm 2.3”无法对应送审稿所称结果，不能通过附件要求的黑箱引用审计。

这些问题都有明确且局部的修复方式，因此裁决为 **GATE-A CONDITIONAL**，而不是 BLOCKED。

---

## 1. 精确陈述与符号审计

### 1.1 可接受的修订版定理

以下版本是本审稿实际确认的命题。

> **定理（严格低阶对称伪微分扰动的无穷小型界）。** 设 \(M\) 为闭光滑 Riemann 流形，\(m>0\)。设 \(P\in\Psi^m_{\rm cl}(M)\) 非负、自伴，且主符号满足
>
> \[
> h_m(x,\xi)\ge c|\xi|_g^m\qquad(\xi\ne0)
> \]
>
> 其中 \(c>0\)，并设 \(q_P\) 的型域为 \(H^{m/2}(M)\)。设 \(Q\) 形式自伴，且对某个 \(r\in(0,m)\) 有 \(Q\in\Psi^r_{1,0}(M)\)。则 \(q_Q\) 在 \(H^{m/2}(M)\) 上由 Sobolev 对偶配对定义，并且对每个 \(\delta>0\)，存在 \(C_\delta<\infty\) 使
>
> \[
> |q_Q[u]|\le \delta q_P[u]+C_\delta\|u\|^2,
> \qquad u\in H^{m/2}(M).
> \]

原稿的交集假设（把 \(Q\) 的 cl 下标删去后）蕴含该定理的假设：可选

\[
\max\{0,1-m\}<\varepsilon<1,
\qquad r=m-1+\varepsilon\in(0,m).
\]

更一般地，若只知 \(Q\in\Psi^{r_0}\) 且 \(r_0<m\)，可先任选
\(\max\{r_0,0\}<r<m\)；普通 Hörmander 类的过滤性给出
\(Q\in\Psi^r\)，故上述版本仍适用。

### 1.2 classical 类的硬性记号问题

标准经典符号 \(S^a_{\rm cl}\) 的齐次展开次数为 \(a,a-1,a-2,\ldots\)。因此经典类并不按任意实数阶差形成原稿所使用的简单过滤：例如一阶符号 \(\xi\) 在通常定义下不因 \(1<1+\varepsilon\) 就自动成为 \(S^{1+\varepsilon}_{\rm cl}\) 的经典符号。当 \(0<\varepsilon<1\) 时，若把最高 \(1+\varepsilon\) 次齐次项设为零，经典展开定义下一步就要求余项属于 \(S^\varepsilon\)，而 \(\xi\notin S^\varepsilon\)。

所以原稿的陈述

\[
i\frac d{dx}\in\Psi^{1+\varepsilon}_{\rm cl}(S^1)
\quad\text{“trivially”}
\]

在标准严格记号下不成立。对数符号（如 \(\log\langle\xi\rangle\)）同样通常不是经典符号，却属于每个正阶的普通 \(S^\varepsilon_{1,0}\)。最小修复是：

\[
Q\in\bigcap_{0<\varepsilon<1}\Psi^{m-1+\varepsilon}_{1,0}(M),
\]

不写 cl；或者完整定义作者采用的“阶数不超过 \(a\) 的 classical/log-classical 过滤类”。

### 1.3 “等价于严格低阶”不成立

原稿写道交集条件“Equivalently, \(Q\) has order strictly less than \(m\)”。这不是等价：例如一个真正的 \(m-\tfrac12\) 阶符号一般不属于 \(\Psi^{m-1+\varepsilon}\) 对所有小 \(\varepsilon>0\)。正确关系是：

\[
Q\in\bigcap_{0<\varepsilon<1}\Psi^{m-1+\varepsilon}
\quad\Longrightarrow\quad
Q\in\Psi^r\text{ for some }r<m,
\]

而反向蕴含一般不成立。证明本身只需右侧较弱条件。

### 1.4 二次型的定义

取 \(0<r<m\)。映射定理给出

\[
Q:H^{r/2}(M)\longrightarrow H^{-r/2}(M).
\]

因此正确的定义是

\[
q_Q[u,v]
:={}_{H^{-r/2}}\!\langle Qu,v\rangle_{H^{r/2}},
\qquad u,v\in H^{m/2}(M)\hookrightarrow H^{r/2}(M),
\]

并令 \(q_Q[u]=q_Q[u,u]\)。该定义先在 \(C^\infty(M)\) 上与 \(L^2\) 内积一致，再由连续性和稠密性唯一延拓。形式自伴性保证延拓后的型为 Hermitian 型。

---

## 2. 被引结果审计

| 原稿引用 | 审计结果 | 结论/最小修复 |
|---|---|---|
| “Hörmander 1968”用于 Sobolev 映射 | **未通过精确引用审计。** 未给论文题目或定理号；Hörmander 1968 年著名的 Acta Math. 论文是 *The spectral function of an elliptic operator*，不是原稿所给映射定理的可识别精确出处。 | 给出完整版本、标题、定理号；或改引 Taylor 短课笔记 I.(3.31)，再说明用 §I.8 的坐标局部化传到闭流形。 |
| Shubin, *Pseudodifferential Operators and Spectral Theory*, “Thm 2.2” | **编号不能确认且高度不匹配。** Springer 2001 二版的基础章把有界性置于 §6、Sobolev 空间置于 §7；“Thm 2.2”不是可核验的所述闭流形 Sobolev 映射引用。 | 删除该编号，补精确版次、页码与正确命题号。 |
| Lions–Magenes；Triebel, *Theory of Function Spaces*, §2.4.2 | 结论正确，但引用不精确。Triebel §2.4.2 的目录主题是 \(\mathbb R^n\) 上 \(B/F\) 空间的实插值，不是原稿所写闭流形谱 Sobolev 范数的逐字命题。 | 本件无需黑箱：直接用 \(I-\Delta_g\) 的谱分解和 Hölder 不等式证明，且得到常数 \(1\)。 |
| “Hörmander 1979；Shubin Thm 3.3；Taylor PDE II Thm 2.3”用于 (3) | 强制性估计正确，但引用未达到精确性要求。Shubin §3 是符号代数而非所称 Gårding 章节；Taylor 出版商目录把 Sobolev 映射放在该章 §5、Gårding 放在 §6，故“Thm 2.3”至少缺章号/版次且不能对应。 | 可改引 Taylor 短课笔记 I.(4.18)–I.(4.19)，并说明闭流形上由有限坐标分割得到同一估计；或补入其他来源的精确定理号。 |
| Calderón–Vaillancourt | 数学用途正确：标准零阶 \(S^0_{1,0}\) 伪微分算子 \(L^2\)-有界。原始论文为 Calderón–Vaillancourt (1972), *A Class of Bounded Pseudo-Differential Operators*, PNAS 69, 1185–1187。 | 可保留，但低阶分支必须改为 \(0<m<1\)，或直接不用此分支。 |

可独立核查的来源列于文末。书目问题不否定数学结论，但按本件送审规则，错误/不可识别的定理编号必须先修复，故不能 PASS。

---

## 3. 四步证明链逐项裁决

### Step 1 — Sobolev 映射与对偶：**CONDITIONAL CONFIRMED**

令 \(r=m-1+\varepsilon\)。标准映射定理确实给出

\[
Q:H^t(M)\to H^{t-r}(M),\qquad t\in\mathbb R.
\]

取 \(t=r/2\)，得到

\[
Q:H^{r/2}\to H^{-r/2}.
\]

于是

\[
|q_Q[u]|
\le \|Q\|_{H^{r/2}\to H^{-r/2}}\,
     \|u\|_{H^{r/2}}^2.
\tag{S1}
\]

所以原稿的指标计算正确；但必须把 \(q_Q\) 明确为对偶配对，并修正 \(Q\) 的符号类和引用。

### Step 2 — 插值：**原量词下 REFUTED；选择 \(\varepsilon\) 后 CONFIRMED**

原稿声称

\[
0<m-1+\varepsilon<m
\quad\text{对所有 }m>0,\ 0<\varepsilon<1.
\]

反例：\(m=2/5,\ \varepsilon=1/10\) 时 \(m-1+\varepsilon=-1/2\)，从而原稿的

\[
\theta=\frac{m-1+\varepsilon}{m}=-\frac54
\]

不在 \((0,1)\)。

最小修复是先选择

\[
\max\{0,1-m\}<\varepsilon<1.
\tag{E}
\]

则 \(r=m-1+\varepsilon\in(0,m)\)，且 \(\theta=r/m\in(0,1)\)。

由于原稿采用谱 Sobolev 范数，插值常数可精确取 \(1\)。设 \(A=I-\Delta_g\)，用其离散谱展开并应用 Hölder：

\[
\|u\|_{H^{r/2}}^2
\le
\bigl(\|u\|_{H^{m/2}}^2\bigr)^\theta
\bigl(\|u\|^2\bigr)^{1-\theta}.
\]

对 \(X,Y\ge0\) 及 \(\eta>0\)，精确的缩放 Young 不等式为

\[
X^\theta Y^{1-\theta}
\le \eta X+(1-\theta)
\left(\frac{\theta}{\eta}\right)^{\theta/(1-\theta)}Y.
\]

因此原稿要求的显式常数是

\[
\boxed{
C(\eta,\theta)
=(1-\theta)
\left(\frac{\theta}{\eta}\right)^{\theta/(1-\theta)}.}
\tag{S2}
\]

该常数也是标量不等式 \(t^\theta\le \eta t+C\) 的最小常数。

### Step 3 — 椭圆强制性估计：**实质 CONFIRMED；依赖声明须修正**

所需结论

\[
q_P[u]\ge c_0\|u\|_{H^{m/2}}^2-C_P\|u\|^2
\tag{S3}
\]

是标准强椭圆 Gårding 估计。可如下独立得到其正系数。

令 \(\Lambda=(I-\Delta_g)^{1/2}\)。\(\Lambda^m\) 的主符号为 \(|\xi|_g^m\)。于是

\[
R:=P-\frac c2\Lambda^m
\]

具有非负主符号。sharp Gårding 给出某个 \(C_G<\infty\)，使

\[
\langle Ru,u\rangle
\ge -C_G\|u\|_{H^{(m-1)/2}}^2.
\]

若 \(m>1\)，再用一次插值并吸收该项；若 \(0<m\le1\)，则
\(\|u\|_{H^{(m-1)/2}}\le\|u\|\)。统一地可取例如

\[
c_0=\frac c4>0
\]

并得到某个 \(C_P\)。所以“\(c_0\) 与 \(c\) 成比例”可以成立（固定度量、量子化、坐标分割后）。

但是，sharp Gårding 的余项常数 \(C_G\)，从而最终 \(C_P\)，一般依赖 \(P\) 的有限个完整符号半范数、坐标图/分割与量子化；这些半范数包括主符号的导数。原稿的“\(C_1'\) 只依赖低阶项”没有根据，必须删除。后文令 \(C_P=C_1'\)。

### Step 4 — 合并：**CONFIRMED（在前述修复后）**

令

\[
C_Q:=\|Q\|_{H^{r/2}\to H^{-r/2}}.
\]

若 \(C_Q=0\)，则 \(q_Q=0\)，结论平凡。以下设 \(C_Q>0\)。由 (S1)、(S2)、(S3)，对任意 \(\eta>0\)，

\[
\begin{aligned}
|q_Q[u]|
&\le C_Q\|u\|_{H^{r/2}}^2\\
&\le C_Q\eta\|u\|_{H^{m/2}}^2
  +C_Q C(\eta,\theta)\|u\|^2\\
&\le \frac{C_Q\eta}{c_0}q_P[u]
 +\left(\frac{C_Q\eta}{c_0}C_P
 +C_QC(\eta,\theta)\right)\|u\|^2.
\end{aligned}
\]

给定目标 \(\delta>0\)，取

\[
\eta=\frac{\delta c_0}{C_Q}.
\]

于是

\[
|q_Q[u]|\le\delta q_P[u]+C_\delta\|u\|^2,
\]

其中

\[
\boxed{
C_\delta
=C_Q(1-\theta)
\left(\frac{\theta C_Q}{\delta c_0}\right)^{\theta/(1-\theta)}
+\delta C_P.}
\tag{S4}
\]

这与原稿公式 (4)

\[
C_\delta=C_Q C(\delta c_0/C_Q,\theta)+\delta C_P
\]

完全一致。

若 \(C_Q>0\) 且 \(0<\theta<1\)，这个**由该证明构造出的**常数以
\(\delta^{-\theta/(1-\theta)}\) 发散。但不能声称所有 \(Q\) 的最优常数都必须发散：若 \(Q\) 本来就是 \(L^2\)-有界（尤其 \(Q=0\)），可取与 \(\delta\) 无关的常数。

---

## 4. 低阶情形审计

### 4.1 原稿的 \(m\le1\) 分支在端点失败

阶数算术是

\[
m-1+\varepsilon\le0
\quad\Longleftrightarrow\quad
m\le1-\varepsilon,
\]

不是 \(m\le1\)。当 \(m=1\) 时，任意 \(\varepsilon>0\) 都给出正阶 \(\varepsilon\)。

这不是纯形式瑕疵。令 \(M=S^1\)、\(P=(I-\Delta)^{1/2}\)（一阶正椭圆），并令

\[
Q=\log (I-\Delta)^{1/2}.
\]

在 Fourier 模 \(e^{inx}\) 上，\(Q\) 的本征值为
\(\tfrac12\log(1+n^2)\)，故 \(Q\) 不在 \(L^2\) 上有界；但其符号属于每个 \(S^\varepsilon_{1,0}\)，\(\varepsilon>0\)。因此原稿在 \(m=1\) 处的 \(L^2\)-有界推论确实错误。

### 4.2 两种正确修法

1. **推荐：完全删除特殊分支。** 对每个 \(m>0\) 选择满足 (E) 的 \(\varepsilon\)，则 Steps 1–4 统一适用。
2. 保留更强的低阶观察，但只写 \(0<m<1\)：选择 \(0<\varepsilon\le1-m\)，即可令 \(m-1+\varepsilon\le0\)，从而 \(Q\in\Psi^0\) 且 \(L^2\)-有界。\(m=1\) 必须回到插值证明。

---

## 5. \(S^1\) 数值/代数锚点复核

设 \(u_n=e^{inx}/\sqrt{2\pi}\)。则

\[
Pu_n=(n^2+1)u_n,
\qquad Qu_n=-nu_n,
\]

所以

\[
q_P[u_n]=n^2+1,
\qquad |q_Q[u_n]|=|n|.
\]

这些计算以及

\[
|n|\le\frac12(n^2+1)
\]

均正确。对于任意 \(\delta>0\)，原稿最终使用的

\[
|n|\le\delta(n^2+1)+\frac1{4\delta}
\tag{A}
\]

也是正确的，因为正确的恒等式是

\[
\delta n^2-|n|+\delta+\frac1{4\delta}
=\delta\left(|n|-\frac1{2\delta}\right)^2+\delta\ge0.
\]

原稿右端漏写了最后的 \(+\delta\)。

但是，\(1/(4\delta)\) 不是原稿所称的“optimal \(C_\delta\)”。最小非负常数是

\[
C_\delta^{\rm opt}
=\max\left\{0,\sup_{n\in\mathbb Z}
\bigl(|n|-\delta(n^2+1)\bigr)\right\}.
\]

整数极值点只需在最接近 \(1/(2\delta)\) 的两个非负整数中检查；除特殊 \(\delta\) 外，并不会“attain at \(1/(2\delta)\)”。把 \(n\) 暂时放宽为实数所得的上界是

\[
\max\left\{0,\frac1{4\delta}-\delta\right\},
\]

而非 \(1/(4\delta)\)。

另一方面，\(1/(4\delta)\) 正是用 \(\theta=1/2\) 的插值 Young 常数 (S2) 所得到的**有效证明常数**，因此它与 (S4) 相符。应把“optimal”改为“the explicit (generally non-optimal) constant produced by (4)”。

本审稿另以有理算术复核了若干锚点：

| \(\delta\) | 整数模上的最小非负 \(C_\delta\) | (S4) 给出的 \(1/(4\delta)\) |
|---:|---:|---:|
| \(1/10\) | \(12/5\)（在 \(|n|=5\)） | \(5/2\) |
| \(1/3\) | \(1/3\)（在 \(|n|=1,2\)） | \(3/4\) |
| \(1/2\) | \(0\) | \(1/2\) |
| \(2\) | \(0\) | \(1/8\) |

表格直接显示：原稿常数有效，但一般并非最优。

---

## 6. 证明链连接、非平凡性与非循环性

### 6.1 链接检查

修复后各环节输入输出完全匹配：

1. 选取 \(r\in(0,m)\)；
2. 映射定理把 \(q_Q\) 控制为 \(H^{r/2}\) 范数平方；
3. 谱插值把 \(H^{r/2}\) 控制为任意小倍数的 \(H^{m/2}\) 加 \(L^2\)；
4. 椭圆 Gårding 估计把 \(H^{m/2}\) 控制为 \(q_P+L^2\)；
5. 选取 \(\eta=\delta c_0/C_Q\)，得到任意目标相对界。

不存在方向颠倒、遗漏项或依赖于待证结论的步骤。

### 6.2 非平凡性

结论不是空泛的：\(S^1\) 上 \(P=-d^2/dx^2+1\)、\(Q=i\,d/dx\) 是非零、无界的 \(Q\)，却对 \(P\) 具有相对型界 \(0\)。\(m=1\) 的 \(\log(I-\Delta)^{1/2}\) 例子还说明插值分支确有必要。

### 6.3 非循环性

**PASS。** 全部论证只使用闭流形上的伪微分 Sobolev 映射、谱插值、Gårding 不等式和标量 Young 不等式。没有出现 \(\zeta\) 函数、零点、Euler 乘积、零点计数、RH 或 RH 等价命题。没有隐藏的数论输入。

### 6.4 解析步骤与有限锚点的分离

**PASS（在删去“optimal”后）。** \(S^1\) Fourier 模计算只是 sanity check，不承担一般定理的证明。一般证明由连续的函数分析估计完成；整数模极值不被用作其输入。

### 6.5 范围与“逃逸”声明

修订后的定理覆盖所有 \(m>0\)。原稿不能再声称其未修订的 Step 2 或“\(m\le1\)”分支已覆盖全部范围。正确覆盖来自对 \(\varepsilon\) 的先验选择 (E)。没有依赖有限维截断或谱逃逸假设。

---

## 7. 必须先完成的确切文字修改

以下全部完成后，本件可提升为 **GATE-A PASS / INDEPENDENTLY-CHECKED**。

1. **修正 \(Q\) 的符号类。** 全文将
   \[
   Q\in\bigcap\Psi^{m-1+\varepsilon}_{\rm cl}(M)
   \]
   改为
   \[
   Q\in\bigcap\Psi^{m-1+\varepsilon}_{1,0}(M),
   \]
   或给出明确、与对数多齐次符号及圆周例子相容的自定义过滤记号。
2. **删除错误的“Equivalently”。** 改成：“This assumption implies membership in some \(\Psi^r\) with \(r<m\); the proof only uses that weaker consequence.”
3. **修正二次型定义。** 把 \(q_Q[u]=\langle Qu,u\rangle\) 明确写成 \(H^{-r/2}\)-\(H^{r/2}\) 对偶配对的连续延拓。
4. **修正 \(\varepsilon\) 的量词。** 在 Step 1 前写：“Choose \(\varepsilon\in(\max\{0,1-m\},1)\), and put \(r=m-1+\varepsilon\), \(\theta=r/m\).” 不得再写对任意 \(\varepsilon\in(0,1)\) 都有 \(\theta\in(0,1)\)。
5. **补入精确 Young 常数。** 使用 (S2)。
6. **修正 Step 3 的依赖声明。** 把“\(C_1'\) only depends on lower-order terms”改为：“\(C_1'\) depends on finitely many seminorms of the full symbol of \(P\), as well as the fixed metric, atlas, partition and quantization; \(c_0\) may be chosen proportional to \(c\).”
7. **处理 \(C_Q=0\)。** 在令 \(\eta=\delta c_0/C_Q\) 前单列 \(C_Q=0\) 的平凡情形。
8. **修正发散声明。** 只声称 (S4) 中由插值构造的常数在 \(C_Q>0\)、\(0<\theta<1\) 时发散；不得把这说成最优常数的必然性质。
9. **删除或修正“\(m\le1\)”特例。** 推荐完全删除；若保留，范围改成 \(0<m<1\)，并说明 \(m=1\) 使用主插值证明。
10. **修正数值锚点。** 保留 (A)，删除“optimal”；将平方恒等式改成带额外 \(+\delta\) 的正确式，并说明整数最优值的定义。
11. **修复书目。** 每个载荷性黑箱必须补全作者、标题、年份、版次、精确命题/公式号和页码；不得保留当前无法对应的 “Shubin Thm 2.2 / 3.3” 或含混的 “Taylor Thm 2.3”。
12. **修改 acceptance statement。** 不得写在未定义的严格 cl 交集下“\(C_\delta\) given by (4)”已无条件确认；应采用 §1.1 的修订陈述，并把 \(C_\delta\) 写成 (S4)，注明它依赖所选 \(r\)（或 \(\varepsilon\)）。

---

## 8. Gate-A 逐项回答

| Gate-A 问题 | 回答 |
|---|---|
| 是否存在隐藏间隙？ | **有。** \(\varepsilon\) 量词、\(m=1\) 低阶端点、二次型配对及 cl 类记号均需修复。 |
| 是否存在循环或 RH 输入？ | **无。** 非循环性 PASS。 |
| 结论是否非平凡？ | **是。** \(S^1\) 的一阶无界扰动例子验证非平凡性。 |
| 分析证明与有限数值锚点是否分离？ | **是。** 锚点不是证明输入；但其“最优”声明须更正。 |
| 所有 \(m>0\) 是否被诚实覆盖？ | **当前文本否；修订后是。** 关键是先选 \(\varepsilon>\max(0,1-m)\)。 |
| 引用是否达到精确黑箱标准？ | **否。** 多个年份/定理号不可对应，须按 §7(11) 修复。 |
| 最小修复后主定理是否成立？ | **是。** §3 给出完整独立证明与显式常数。 |

## 9. 最终裁决

### **GATE-A CONDITIONAL**

送审稿的核心命题经独立核验为真，且修订后的四步链在所有 \(m>0\) 上闭合；没有 RH、数论或循环输入。但原稿包含若干明确的假陈述和不可审计引用，故不能原样进入 INDEPENDENTLY-CHECKED。

**提升为 GATE-A PASS 的充分且必要条件：** 完成 §7 的 12 项文字修改，尤其是 cl 类、\(\varepsilon\) 量词、\(m=1\) 端点、数值锚点和精确引用五项。无需新增数学假设，也无需改变 Paper B 所需的最终型有界结论。

---

## 10. 核查来源

1. Michael E. Taylor, *Short Course on Pseudodifferential Operators*：普通符号定义与 classical 展开见 I.(1.15)–I.(1.17)；Sobolev 映射见 I.(3.31)；强椭圆 Gårding 见 I.(4.18)–I.(4.19)；闭流形局部化见 §I.8。  
   https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2022/05/psidolect.pdf
2. M. A. Shubin, *Pseudodifferential Operators and Spectral Theory*, 2nd ed., Springer, 2001；官方书目信息及章节结构。  
   https://link.springer.com/book/10.1007/978-3-642-56579-3
3. Michael E. Taylor, *Partial Differential Equations II*, chapter “Pseudodifferential Operators”；出版商目录明确把 Sobolev 映射置于 §5、Gårding 置于 §6。  
   https://link.springer.com/chapter/10.1007/978-1-4757-4187-2_1
4. Lars Hörmander, “The spectral function of an elliptic operator,” *Acta Mathematica* 121 (1968), 193–218。  
   https://projecteuclid.org/journals/acta-mathematica/volume-121/issue-none/The-spectral-function-of-an-elliptic-operator/10.1007/BF02391913.short
5. Alberto P. Calderón and Rémi Vaillancourt, “A Class of Bounded Pseudo-Differential Operators,” *PNAS* 69 (1972), 1185–1187。  
   https://www.pnas.org/doi/10.1073/pnas.69.5.1185
6. Hans Triebel, *Theory of Function Spaces* (1983)，目录 §2.4.2。  
   https://d-nb.info/830874283/04

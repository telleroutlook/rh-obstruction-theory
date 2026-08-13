# OB-33 独立审稿裁决：D′ narrowed \(\mathcal C_{\mathrm{logpoly}}^{\mathrm{sub,ell}}\) leading-singularity lemma

**审稿对象：** `OB-33-Dprime-subell-lemma-gate-a.md`  
**审稿方式：** 不预设作者结论；逐项核对定义、量词、引文范围、谱渐近、Tauber 步骤、反例常数与 RH 非循环性。  
**最终裁决：** **GATE-A CONDITIONAL**。  
**状态建议：** 在下文 M1–M9 全部落实前，不得把该包标为 `INDEPENDENTLY-CHECKED`；落实后，核心的 narrowed lemma 可以晋级，而 D′ 整体仍应保持 `ESCAPE-ROUTE-REFINED`，Claim E 继续开放。

---

## 1. 裁决摘要

核心结论

\[
N_H(\Lambda)\sim C_H\Lambda^{d/m},\qquad
\operatorname{Tr}(e^{-tH})\sim
\Gamma(1+d/m)C_Ht^{-d/m}
\]

在一个**明确规定为标量、标准 log-polyhomogeneous 符号类、自然自伴闭包**的 narrowed class 中是正确的；低阶对数项不会改变主 Weyl 系数。因此，“首项是正系数纯幂、不能等于 zeta-ordinate 热和的 \(t^{-1}\log(1/t)\) 首项”这一核心命题可修复成立，也没有使用 RH。

但送审稿的现有证明与部分附带断言不能照收：

1. \(H\ge -C\) 并不保证未平移的 \(H^{1/m}\) 有实的正分数幂；
2. 含 \(|\xi|^{m-1}\log|\xi|\) 的 \(H\) 通常不是 classical ΨDO，其分数幂通常仍含对数项，Seeley 的 classical 结论不能原样套用；
3. 所写强余项
   \[
   O\!\left(\Lambda^{(d-1)/m}\right)
   \]
   对该类是假的；低阶对数项可以产生额外的 \(\log\Lambda\)；
4. Hörmander (1968) Theorem 1.1 的对象与送审稿所称的“正的一阶 classical ΨDO”不一致；正确的一阶 ΨDO 结果在 Theorem 4.4，且其主积分使用的是**完整一阶符号的次水平集**，不是直接把完整符号换成齐次主符号后仍保留相同余项；
5. \(\{\gamma_n\}\) 未在“自包含定义”中精确定义。必须明确它是所有非平凡零点的正虚部多重集，而不是临界线零点序列；
6. “\(\operatorname{vol}\{h_m\le1\}\) 有限当且仅当椭圆”这一附带说法一般不成立；椭圆性在此是保证全类结论的充分条件，反例只证明去掉它后全称命题失败；
7. 数值锚点缺少参数和脚本，七个小数不可重放。

因此，这是“主结论可修、当前文字与证明尚未过 Gate”的典型 **CONDITIONAL**，而不是 PASS；也没有发现必须借助 RH 才能修复的障碍，故不判 BLOCKED。

---

## 2. 精确陈述、量词与符号审计

| 项目 | 当前状态 | 独立判断 | 必须处理 |
|---|---|---|---|
| \(M,d,m,K\) | \(M\) closed，\(d\ge1\)，\(m>0\)，但 \(K\) 未量化 | 不完整 | 写明 \(K\in\mathbb N_0\) 固定且有限 |
| 作用空间 | 未说明 \(H\) 作用于函数还是向量丛，也未固定密度 | 不完整且影响 \(C_H\) | 最小修复是限定标量 \(L^2(M,d\mu)\)，固定正光滑密度 \(d\mu\) |
| “positive-definite” | 是矩阵措辞，但常数公式按标量写 | 含混 | 标量版改为 \(h_m(x,\xi)>0\)；若保留系统，常数须改为主符号特征值的计重相空间体积 |
| \(\log|\xi|\) | 未固定余切范数 | 可修 | 固定任一光滑余切范数；不同选择只改变低阶系数 |
| \(h_{m-j,\ell}\) | 未明说齐次度、光滑性 | 不完整 | 写明在 \(|\xi|\ge1\) 上光滑并关于 \(\xi\) 齐次 \(m-j\) 次 |
| 符号中的 `\(\sim\)` | 未给余项及导数估计 | “self-contained” 声明不成立 | 对每个截断阶 \(J\) 给出标准 log-polyhomogeneous 余项估计；减去 \(h_m\) 及 \(1\le j<J\) 的项后，至少保证余项属于每个 \(S^{m-J+\varepsilon}_{1,0}\)，\(\varepsilon>0\) |
| 自伴实现 | 只写 “\(H=H^*\) is a ΨDO” | 域未说明 | 写成定义在 \(C^\infty(M)\) 上的标量、形式自伴椭圆 ΨDO 的自伴闭包 |
| \(Z_H(t)\) | 在证明 trace class 前即写作 trace | 可修 | 先由 Weyl 上界得 \(e^{-tH}\) trace class；或在定义处注明随后由引理证明收敛 |
| \(C_H\) 的体积 | 未说明测度 | 不完整 | 指定余切丛的 canonical Liouville measure（由局部 \(dx\,d\xi\) 表示） |
| \(\{\gamma_n\}\) | 未定义 | 非循环性审计的关键缺口 | 明确定义为所有 \(\rho=\beta+i\gamma\) 的 \(\gamma>0\)，按零点重数计数，不要求 \(\beta=1/2\) |
| “spectrum equals” | 未明说重数 | 不完整 | 写明谱与 \(\{\gamma_n\}\) 作为多重集相等 |

在标量框架下，椭圆性确实给出 \(0<C_H<\infty\)：在余球面上有
\(0<c\le h_m(x,\omega)\le C<\infty\)，故每个纤维中的 \(\{h_m\le1\}\) 被两个正半径球夹住。

---

## 3. 引文逐一核对

### 3.1 Hörmander (1968)

**书目信息确认：** Lars Hörmander, “The spectral function of an elliptic operator,” *Acta Mathematica* **121** (1968), 193–218。原文扫描：[Acta Math. paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6063-11511_2006_Article_BF02391913.pdf)。

**编号与范围：**

- Theorem 1.1 按原文第 193–194 页的设置，是关于正的椭圆**微分算子** \(P\)（一般阶 \(m\)）的局部谱函数余项。送审稿把它陈述为“正自伴一阶 classical elliptic ΨDO 的计数定理”，编号/对象不精确。
- 原文 §§3–4 处理闭流形上的形式自伴、下有界、一阶 type \((1,0)\) 椭圆 ΨDO；Theorem 4.4 给出
  \[
  e(x,x,\lambda)-(2\pi)^{-d}\int_{a'(x,\xi)<\lambda}d\xi
  =O(\lambda^{d-1}),
  \]
  其中次水平集由适配构造中的**完整一阶符号** \(a'\) 决定。
- 原文第 215 页、Theorem 5.1 的证明用 Seeley 的复幂把高阶 classical 情形降到一阶。

**适用性裁决：** Hörmander 的结果支持 classical 比较算子的 Weyl 定律，也支持“完整符号次水平集 + sharp remainder”；它不支持把含 \(\log|\xi|\) 的完整符号直接丢掉后仍声称
\(O(\Lambda^{(d-1)/m})\)。因此送审稿对该引文**用超范围**。

### 3.2 Seeley (1967)

**书目信息确认：** R. T. Seeley, “Complex powers of an elliptic operator,” in *Singular Integrals*, Proc. Sympos. Pure Math. **10**, AMS, 1967, 288–307，MR 0237943。AMS 卷页：[PSPUM 10](https://pubs.ams.org/ebooks/pspum/010/)。

**范围：** Seeley 的构造位于 classical elliptic ΨDO 的带参数演算中，并需要可用的谱切割；正、可逆情形是标准特例。送审稿没有给出该文中所依赖结论的精确编号或页内定位，因此未达到其自己要求的 L17 引文标准。

**适用性裁决：** 当前 \(H\) 允许低阶 log-polyhomogeneous 项，一般不是 classical；且仅假设 \(H\ge-C\)，可能有负特征值。故“Seeley 直接推出 \(H^{1/m}\) 是 classical order-one ΨDO”是错误的。即使先平移为正，分数幂通常仍是 log-polyhomogeneous，而不是 classical。等式
\(N_{H^{1/m}}(\lambda)=N_H(\lambda^m)\) 本身来自正算子的谱演算，并非无需正性即可使用。

### 3.3 Bingham–Goldie–Teugels (1987)

**书目信息确认：** N. H. Bingham, C. M. Goldie, J. L. Teugels, *Regular Variation*, Cambridge University Press, 1987, Theorem 1.7.1（Karamata Tauberian theorem for Laplace–Stieltjes transforms）。章节与 DOI：[Karamata Theory](https://doi.org/10.1017/CBO9780511721434.003)。

**范围：** 对非减、右连续的 \(U\) 及慢变函数 \(L\)，该定理给出
\[
U(x)\sim Cx^\rho L(x)
\quad\Longleftrightarrow\quad
\int_{[0,\infty)}e^{-tx}\,dU(x)
\sim C\Gamma(1+\rho)t^{-\rho}L(1/t)
\]
（按常数的等价归一化书写），这里 \(\rho\ge0\)。

**适用性裁决：** 对计数函数的使用正确，但必须先处理 \(H\) 的有限负谱：取 \(b\) 使 \(H+b\ge1\)，对 \(N_{H+b}\) 应用定理，再用
\(Z_H(t)=e^{bt}Z_{H+b}(t)\)。送审稿漏写了这一步。

### 3.4 Riemann–von Mangoldt

送审稿使用了该结果，却未在 “Allowed premises” 中给出作者/年份/编号。可审计引用应补为：E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., revised by D. R. Heath-Brown, Oxford, 1986, Theorem 9.4（Theorem 9.3 给出含 \(S(T)\) 的更精细形式）。其无条件结论是

\[
N_\zeta(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T).
\]

这里计数的是临界带中所有 \(0<\Im\rho\le T\) 的非平凡零点，按重数计；没有临界线限制。NIST 对“所有临界带零点”与“临界线零点”的区分可见 [DLMF §25.10](https://dlmf.nist.gov/25.10)。

---

## 4. Link A：主符号、复幂与 Weyl 首项

### A1. 低阶对数项不进入主符号——确认

对 \(j\ge1\)、\(0\le\ell\le K\)，令 \(r=|\xi|\)。则

\[
\frac{r^{m-j}(\log r)^\ell}{r^m}
=r^{-j}(\log r)^\ell\longrightarrow0.
\]

对任意 \(\xi\)-导数也有同样的一阶亏损：

\[
\partial_\xi^\beta
\bigl(h_{m-j,\ell}(x,\xi)(\log r)^\ell\bigr)
=O\!\left(r^{m-j-|\beta|}(\log r)^\ell\right),
\]

加上较低 log 次数的项。因此，在 M1 所要求的标准余项估计下，完整余项在缩放 \(\xi=\Lambda^{1/m}\eta\) 后相对 \(\Lambda\) 一致趋零；首相空间体积只由 \(h_m\) 决定。此链节 **PASS**。

### A2. “\(H^{1/m}\) 是 classical”——否定

取 \(M=\mathbb T^1=\mathbb R/(2\pi\mathbb Z)\)，令 \(D_x=-i\partial_x\)，并令

\[
H=(1+D_x^2)^{1/2}+\tfrac12\log(1+D_x^2).
\]

其标量符号为

\[
\sqrt{1+\xi^2}+\tfrac12\log(1+\xi^2)
=|\xi|+\log|\xi|+O(|\xi|^{-1}),
\]

故 \(d=m=1\)，主符号 \(h_1=|\xi|\)，而 order-zero log 项严格位于主阶以下。这里 \(H^{1/m}=H\) 本身就不是 classical。因而送审稿 Step 1 的 “classical” 断言是一个直接可复核的反例。该链节 **FAIL as written**。

### A3. 首 Weyl 渐近——可修复确认

不需要对 log-polyhomogeneous \(H\) 使用 Seeley。可采用如下比较证明。

选取一个正的、标量、classical elliptic ΨDO \(P\)，阶数也是 \(m\)，且主符号同为 \(h_m\)。由 classical elliptic ΨDO 的 Weyl 定律（可由 Hörmander (1968), Theorem 4.4 对正的一阶算子应用；一般正阶通过同文第 215 页所述的 classical 复幂降阶），

\[
N_P(\Lambda)\sim C_H\Lambda^{d/m}.
\]

按 M1 的符号余项定义，对任一固定 \(0<\varepsilon<1\)，
\(R:=H-P\in\Psi^{m-1+\varepsilon}_{1,0}\)。椭圆估计、Sobolev 插值与 \(R\) 的形式有界性给出：对每个 \(0<\delta<1\)，存在 \(C_\delta\) 使

\[
(1-\delta)P-C_\delta
\le H\le
(1+\delta)P+C_\delta
\]

作为二次型成立。min–max 原理于是给出

\[
N_P\!\left(\frac{\Lambda-C_\delta}{1+\delta}\right)
\le N_H(\Lambda)
\le
N_P\!\left(\frac{\Lambda+C_\delta}{1-\delta}\right).
\]

先令 \(\Lambda\to\infty\)，再令 \(\delta\downarrow0\)，得到

\[
N_H(\Lambda)\sim C_H\Lambda^{d/m}.
\]

这证明核心首项，而不声称不真实的 sharp remainder。

### A4. 所写 \(O(\Lambda^{(d-1)/m})\)——否定

继续使用 A2 的 \(\mathbb T^1\) 算子。其特征值为

\[
\lambda_k=\sqrt{1+k^2}+\log\sqrt{1+k^2},\qquad k\in\mathbb Z.
\]

方程 \(r+\log r=\Lambda\) 的解满足
\(r=\Lambda-\log\Lambda+O((\log\Lambda)/\Lambda)\)。因此

\[
N_H(\Lambda)=2\Lambda-2\log\Lambda+O(1).
\]

而送审稿的公式在 \(d=m=1\) 时声称 \(N_H(\Lambda)=2\Lambda+O(1)\)，矛盾。故 Link A 中的强余项必须删除，或另行证明一个允许 log 因子的较弱余项。核心引理只需 `\(\sim\)`。

---

## 5. Link B：Karamata 到热迹

令 \(\rho=d/m>0\)。取 \(b\) 充分大使 \(H+b\ge1\)。由 Link A 的已修复首项，

\[
N_{H+b}(\Lambda)=N_H(\Lambda-b)
\sim C_H\Lambda^\rho.
\]

计数函数非减、右连续，且相应 Laplace–Stieltjes 变换就是 \(Z_{H+b}(t)\)。BGT Theorem 1.7.1 给出

\[
Z_{H+b}(t)
\sim C_H\Gamma(1+\rho)t^{-\rho}.
\]

再由 \(Z_H(t)=e^{bt}Z_{H+b}(t)\) 及 \(e^{bt}=1+o(1)\)，

\[
Z_H(t)=a_0t^{-d/m}+o(t^{-d/m}),
\qquad
a_0=\Gamma(1+d/m)C_H>0.
\]

故 Link B 在补入平移步骤后 **PASS**。该渐近严格排除了同阶的
\(t^{-d/m}\log(1/t)\)；它不排除严格次阶的对数项。

---

## 6. Link C：\(\mathbb T^4\) 非椭圆反例

### 6.1 算子与符号——确认并修正文句

取 \(\mathbb T^2=\mathbb R^2/(2\pi\mathbb Z)^2\)，
\(\mathbb T^4=\mathbb T_x^2\times\mathbb T_y^2\)，

\[
H=(I-\Delta_x)(I-\Delta_y).
\]

其特征值为

\[
(1+|p|^2)(1+|q|^2),\qquad p,q\in\mathbb Z^2,
\]

算子正、自伴且有紧预解。四阶主符号
\(h_4(\xi_x,\xi_y)=|\xi_x|^2|\xi_y|^2\) 在
\(\xi_x=0\) 或 \(\xi_y=0\) 的两个坐标二维子空间上消失。因此附件中的 “vanishes off the axes” 应改为 “vanishes on the coordinate subspaces \(\{\xi_x=0\}\cup\{\xi_y=0\}\)” 。

### 6.2 计数常数——精确确认

记

\[
A(X)=\#\{p\in\mathbb Z^2:1+|p|^2\le X\}.
\]

用单位方格夹逼圆盘，得到初等且足够的

\[
A(X)=\pi X+O(X^{1/2}).
\]

于是

\[
\begin{aligned}
N_H(\Lambda)
&=\sum_{1+|p|^2\le\Lambda}
A\!\left(\frac{\Lambda}{1+|p|^2}\right)\\
&=\pi\Lambda
\sum_{1+|p|^2\le\Lambda}\frac1{1+|p|^2}
+O\!\left(\Lambda^{1/2}
\sum_{1+|p|^2\le\Lambda}(1+|p|^2)^{-1/2}\right).
\end{aligned}
\]

分部求和给出

\[
\sum_{1+|p|^2\le X}\frac1{1+|p|^2}
=\pi\log X+O(1),
\qquad
\sum_{1+|p|^2\le X}(1+|p|^2)^{-1/2}=O(X^{1/2}).
\]

所以

\[
N_H(\Lambda)=\pi^2\Lambda\log\Lambda+O(\Lambda).
\]

该系数与余项均确认。BGT Theorem 1.7.1（\(\rho=1\)，慢变部分 \(\pi^2\log\Lambda\)）继而给出

\[
Z_H(t)\sim\pi^2t^{-1}\log(1/t).
\]

### 6.3 “finite iff elliptic”——否定

椭圆性保证主符号次水平集体积有限，但反命题一般不成立。例如在二维纤维取

\[
h_6(\xi_1,\xi_2)=\xi_1^2(\xi_1^2+\xi_2^2)^2
=r^6\cos^2\theta.
\]

它在 \(\xi_1=0\) 上消失，故不椭圆；但

\[
\operatorname{vol}\{h_6\le1\}
=\frac12\int_0^{2\pi}|\cos\theta|^{-2/3}\,d\theta<\infty.
\]

这也可实现为有紧预解的完整算子：在 \(\mathbb T^2\) 上取
\[
H_*=D_1^2(D_1^2+D_2^2)^2+D_2^4+1.
\]
它正、自伴，特征值沿任意格点逃逸方向趋于无穷，而六阶主符号正是上述非椭圆的 \(h_6\)。

因此可确认的是：“去掉椭圆性后，全类纯幂结论失败；给出的 \(\mathbb T^4\) 例子确实失败。”不能声称“有限体积 iff 椭圆”，也不能声称每个非椭圆算子都必有 leading log。

Link C 因而是 **反例本身 PASS，关于必要性的两句过强文字 FAIL**。

---

## 7. Link D：与 zeta ordinates 比较及非循环性

令 \(\{\gamma_n\}\) 表示所有非平凡零点
\(\rho=\beta+i\gamma\) 中 \(\gamma>0\) 的虚部多重集，零点按解析重数计数；绝不加入 \(\beta=1/2\)。则无条件 Riemann–von Mangoldt 公式给出

\[
N_\zeta(T)=\#\{n:\gamma_n\le T\}
\sim\frac1{2\pi}T\log T.
\]

再次使用 BGT Theorem 1.7.1，

\[
Z_\zeta(t):=\sum_ne^{-t\gamma_n}
\sim\frac1{2\pi}t^{-1}\log(1/t),
\]

因为 \(\Gamma(2)=1\)。

若 \(\operatorname{spec}(H)=\{\gamma_n\}\) 作为多重集成立，则两个计数函数应完全相同。但

\[
C_HT^{d/m}
\not\sim \frac1{2\pi}T\log T
\]

对任何固定 \(d/m>0\) 都成立：若 \(d/m\ne1\)，幂指数不合；若 \(d/m=1\)，还差一个无界的 \(\log T\) 因子。因此排除结论 **PASS**。

### 非循环性检查

| 可能的 RH 泄漏点 | 判断 |
|---|---|
| 把所有零点写成 \(1/2+i\gamma_n\) | 当前附件没有定义，存在措辞风险；M4 必须禁止这种定义 |
| Riemann–von Mangoldt 计数 | 无条件，计数临界带全部零点，不要求零点位于临界线 |
| “\(\gamma_n\) 为实数” | 它们是复数零点的虚部，按定义为实数；不是“zeta 零点本身为实” |
| 谱比较 | 只比较实数多重集及计数增长，不使用 RH 等价命题 |
| Links A–C | 完全属于 ΨDO/谱几何与格点计数，不接触 RH |

结论：按 M4 的精确定义修正后，没有 RH、RH 等价命题或零点位置输入。Q1 可条件确认。

---

## 8. 脚本与数值锚点审计

### 8.1 精确格点计数重放

下列脚本的 `exact_N` 只使用整数运算；浮点比值仅用于显示收敛趋势，不承担证明。解析证明已在 §6.2 给出。

```python
from bisect import bisect_right
from math import isqrt, pi, log

Lmax = 200_000
R = isqrt(Lmax - 1)
vals = []
for p1 in range(-R, R + 1):
    qmax = isqrt(max(0, Lmax - 1 - p1*p1))
    vals.extend(1 + p1*p1 + p2*p2
                for p2 in range(-qmax, qmax + 1))
vals.sort()

for L in [100, 1_000, 10_000, 100_000, 200_000]:
    j = bisect_right(vals, L)
    N = sum(bisect_right(vals, L // a) for a in vals[:j])
    print(L, N, N / (pi*pi*L*log(L)))
```

实际得到：

| \(\Lambda\) | exact \(N_H(\Lambda)\) | \(N_H/(\pi^2\Lambda\log\Lambda)\) |
|---:|---:|---:|
| 100 | 3,505 | 0.771156622500 |
| 1,000 | 58,457 | 0.857432290661 |
| 10,000 | 811,369 | 0.892571437434 |
| 100,000 | 10,392,713 | 0.914625900792 |
| 200,000 | 22,154,633 | 0.919515106910 |

此外，§4.4 的一维 log 例在
\(\Lambda=10^5\) 时精确计数为 \(N_H=199,977\)，故
\(N_H-2\Lambda=-23\)；随 \(\Lambda\) 增大该差按
\(-2\log\Lambda+O(1)\) 无界，直接否定声称的 \(O(1)\) 余项。

### 8.2 附件自己的七个小数——不可核验

“\(+0.039,+0.036,\ldots,+0.015\)”没有给出：

- 满足 \(d/m=1\) 的具体 \(d=m\)；
- 常数 \(c\) 及其符号；
- 起始 \(t\) 和二分网格；
- 求和截断 \(N_{\max}\)；
- 尾项的严格误差界；
- 所称脚本或其哈希。

因此这些小数不能作为“script-verified”证据。可无数值地严格确认的只有：当 \(d=m\) 且 \(c\) 固定时，

\[
\lambda_n=n+c\,n^{1-1/d}\log n=n(1+o(1)),
\]

从而 \(N(\Lambda)\sim\Lambda\) 且 \(tZ(t)\to1\)。若要保留“正增量”措辞，还必须加 \(c>0\)；否则增量符号也未确定。M9 要求删除七个数，或补齐上述全部参数和尾项证书。

---

## 9. Gate-A 问题逐项回答

### Q1 — Non-circularity

**条件确认。** 数学链没有使用 RH；唯一风险是 \(\{\gamma_n\}\) 未定义。按 M4 定义为临界带全部非平凡零点的正虚部后，无泄漏。

### Q2 — Narrowed lemma

**主结论确认，现有证明不确认。**

- sub-principal log 项是 \(o(|\xi|^m)\)：确认；
- 主 Weyl 系数只由 \(h_m\) 决定：确认；
- \(a_0=\Gamma(1+d/m)C_H>0\)：确认；
- 未平移的 \(H^{1/m}\)：不确认；
- “\(H^{1/m}\) classical”：否定；
- \(O(\Lambda^{(d-1)/m})\) 强余项：否定；
- Karamata 步骤：补入平移后确认。

### Q3 — Ellipticity / OB-31 block

**核心确认、措辞需收窄。** \(\mathbb T^4\) 反例、\(\pi^2\) 系数和 leading log 全部确认；这足以证明未加椭圆性的 universal class 不能恢复。当前 lemma 的量词确实只覆盖 narrowed class，未重新断言 OB-31 已否定的 universal claim。但“finite iff elliptic”及“ellipticity 对每个个体都必要”必须删除。

### Q4 — Citation scope

**未通过现稿。**

- Hörmander：作者、年份、期刊正确；Theorem 1.1 的对象被误述，应改引 Theorem 4.4/第 215 页的 classical reduction，并限制结论；
- Seeley：作者、年份、卷页正确；现有 \(H\) 超出 classical 范围，且缺精确页内定位；
- BGT：作者、年份、Theorem 1.7.1 与用途正确，但须先平移负谱；
- Riemann–von Mangoldt：现稿漏引；应补 Titchmarsh–Heath-Brown (1986), Theorem 9.4。

### Q5 — Verdict / status movement

**GATE-A CONDITIONAL。** 现在不能直接推进为 `INDEPENDENTLY-CHECKED`。M1–M9 完成后，可将
`LEADING-SINGULARITY-COVERS-SUBPRINCIPAL-LOGPOLY`
作为 narrowed lemma 推进；D′ 仍保持 `ESCAPE-ROUTE-REFINED`，Claim E 保持开放。

---

## 10. 必须先做的精确文字修改 M1–M9

### M1 — 用可判定的标量 log-polyhomogeneous 类替换当前定义

至少加入以下文字：

> Fix a closed smooth \(d\)-manifold \(M\), \(d\ge1\), a positive smooth density \(d\mu\), and a smooth norm \(|\cdot|\) on \(T^*M\). The operator \(H\) is the self-adjoint closure in \(L^2(M,d\mu)\) of a scalar formally self-adjoint elliptic ΨDO of order \(m>0\). Fix \(K\in\mathbb N_0\). Each \(h_{m-j,\ell}\) is smooth for \(\xi\ne0\) and homogeneous of degree \(m-j\) for \(|\xi|\ge1\). For every \(J\ge1\), after subtracting \(h_m\) and the terms with \(1\le j<J\), the remainder satisfies, for every \(\varepsilon>0\), the symbol estimates of \(S^{m-J+\varepsilon}_{1,0}\). The scalar principal symbol is real and satisfies \(h_m(x,\xi)\ge c|\xi|^m\) for \(|\xi|\ge1\).

并把 \(C_H\) 中的 `vol` 明确为 canonical Liouville volume。

### M2 — 删除强余项

把 Proof Step 2 的

> \(N_H(\Lambda)=C_H\Lambda^{d/m}+O(\Lambda^{(d-1)/m})\)

以及 Link A 中同一要求，统一改为

> \(N_H(\Lambda)=C_H\Lambda^{d/m}+o(\Lambda^{d/m})\).

除非另附允许 log 因子的独立余项定理与证明，不得保留原 \(O\)-式。

### M3 — 整段替换当前三步证明

使用 §4.3 的 classical comparison + infinitesimal form bound + min–max 证明 Weyl 首项，再使用 §5 的平移后 Karamata 证明热迹首项。不得再写“Seeley 直接使当前 \(H^{1/m}\) classical”。

### M4 — 精确定义 zeta 比较序列

在定义区加入：

> Let \(\{\gamma_n\}\) be the multiset of positive imaginary parts \(\gamma>0\) of all nontrivial zeros \(\rho=\beta+i\gamma\) of \(\zeta\), counted with the analytic multiplicity of \(\rho\). No condition \(\beta=1/2\) is imposed.

并把所有“spectrum equals”改成“equals as a multiset”。

### M5 — 修正引文清单

1. Hörmander 项改述为 Theorem 4.4 的一阶 ΨDO 完整符号次水平集公式，并注明 Theorem 1.1 本身是微分算子设置；
2. 采用 M3 的比较证明后，删除 Seeley 作为当前 \(H\) 的直接前提；若仍保留它来说明 classical 比较算子的复幂降阶，须明确限于 classical elliptic operator，并给出所用页内定位；
3. BGT 项保留 Theorem 1.7.1，但在正文写出平移负谱；
4. 新增 Titchmarsh–Heath-Brown (1986), Theorem 9.4 的 Riemann–von Mangoldt 引用。

### M6 — 修正反例的几何措辞

把

> vanishes off the axes

改成

> vanishes on the coordinate subspaces \(\{\xi_x=0\}\cup\{\xi_y=0\}\), hence is not elliptic.

并在第一次出现时固定
\(\mathbb T^2=\mathbb R^2/(2\pi\mathbb Z)^2\)，以锁定 \(\pi^2\) 常数。

### M7 — 删除 “finite iff elliptic” 与过强必要性

把相关句子替换为：

> Ellipticity guarantees \(0<C_H<\infty\) and is load-bearing for this class-wide lemma. In the displayed non-elliptic \(\mathbb T^4\) example the principal-symbol sublevel volume is infinite and the counting law acquires a leading logarithm. This shows that the universal claim without ellipticity is false; it does not assert that every non-elliptic operator has a leading logarithm.

### M8 — 修正“次阶 log”措辞

把

> Subleading \(t^k\log(1/t)\) terms may occur

改为

> Strictly lower-order terms involving powers of \(\log(1/t)\) may occur; no full heat expansion is claimed here.

避免把一般阶 \(m\) 的指数误写成整数 \(k\)。

### M9 — 删除或补齐数值锚点

删除七个无参数小数；或者同时给出 \(d,m,c\)、全部 \(t\)、截断、尾项区间界、可重放脚本及版本/哈希。该段不得继续标注为 “script-verified” 而没有这些信息。

---

## 11. 最终状态语句

当前可记录为：

> **GATE-A CONDITIONAL.** The narrowed pure-leading-power lemma is mathematically correct after (i) defining a scalar standard log-polyhomogeneous elliptic class, (ii) replacing the invalid classical-complex-power argument by a comparison/min–max proof, (iii) deleting the false sharp Weyl remainder, (iv) shifting the finite negative spectrum before Karamata, (v) defining \(\{\gamma_n\}\) as ordinates of all nontrivial zeros without a critical-line assumption, and (vi) correcting the citation and counterexample wording. No RH input is used. After these edits the narrowed lemma may advance to `INDEPENDENTLY-CHECKED`; D′ as a whole remains `ESCAPE-ROUTE-REFINED`, with Claim E open.

这也是本审稿的最终裁决。

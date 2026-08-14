# OB-38 独立审稿裁决：\(T^4\) 上乘积算子的计数函数

**审稿对象：** OB-38-B-torus-lattice.md  
**审稿日期：** 2026-08-14  
**审稿方式：** 独立重建证明、逐式核对、两条整数枚举路线交叉验证；不预设作者结论成立。

## 1. 最终裁决

### 数学命题

**CONFIRMED（经下述校正后）**：对实数 \(\Lambda\to+\infty\)，

\[
N_{H_{\mathrm{prod}}}(\Lambda)
=\pi^2\Lambda\log\Lambda+O(\Lambda).
\]

证明只需要二维格点圆盘估计

\[
B(K):=\sum_{k=0}^{K}r_2(k)=\pi K+O(K^{1/2})
\]

以及有限 Abel 求和。没有使用 RH、RH 的等价命题、
\(\zeta\) 零点、Euler 乘积或 \(\zeta\) 的函数方程。

### 对当前送审文本

**GATE-A CONDITIONAL**。主结论和证明策略正确，但当前文本不能原样标为
INDEPENDENTLY-CHECKED，原因是：

1. Step 2 把 Abel 和中的第二个求和上限从正确的 \(N-2\) 写成了 \(N-1\)；
2. 同一步把 \(B(k)=\pi k+O(k^{1/2})\) 直接用于 \(k=0\)，而 \(B(0)=1\)；
3. 所显示的调和数常数项漏掉了 Euler 常数 \(\gamma\)，因此该行带
   \(O(1/N)\) 的等式不成立；
4. Step 3 的二进壳未处理 \(k=0\)，且取
   \(J=\lfloor\log_2N\rfloor\) 时一般漏掉 \(2^J<k<N\) 的尾壳；
5. Hardy–Wright 与 Ivić 的书目定位混用了两个不同结果，其中
   “Ivić §12.1”不是圆问题位置；
6. \(\Lambda=100\) 的“大 \(O\) 数值容差”表述不成立：未给显式常数的
   \(O(\Lambda)\) 不能解释成误差绝对值至多 \(100\) 或相对误差至多
   \(1/\log100\)。

这些都是可局部修复的问题；没有发现改变主定理、主系数或非循环性的缺口。
完成第 9 节的文字修改后，本件可升级为 **GATE-A PASS**。

---

## 2. 精确陈述、量词与符号核对

1. \(T^2=\mathbb R^2/(2\pi\mathbb Z)^2\) 的约定与 Fourier 模
   \(e^{ip\cdot x}/(2\pi)\) 相容：其 \(L^2([0,2\pi]^2)\)-范数为 \(1\)。
2. \(-\Delta e^{ip\cdot x}=|p|^2e^{ip\cdot x}\)，故
   \(I-\Delta\) 的特征值为 \(1+|p|^2\)。
3. 在张量积基上，
   \(H_{\mathrm{prod}}=(I-\Delta_x)(I-\Delta_y)\) 的特征值确为
   \((1+|p|^2)(1+|q|^2)\)。“每个有序对 \((p,q)\) 计一次”正确；若不同
   有序对给出同一数值特征值，它们应作为谱重数分别计数，而定义中的格点计数正是如此。
4. 对任意实数 \(\Lambda\ge1\)，令 \(N=\lfloor\Lambda\rfloor\)。则
   \(1+k\le\Lambda\) 等价于 \(0\le k\le N-1\)，所以 Step 2 的离散化范围正确。
5. 主张的精确量词应写成：存在 \(C,\Lambda_0>0\)，使所有实数
   \(\Lambda\ge\Lambda_0\) 满足

   \[
   \left|N_{H_{\mathrm{prod}}}(\Lambda)
   -\pi^2\Lambda\log\Lambda\right|\le C\Lambda.
   \]

背景中的“非椭圆”判断也正确：四阶主符号为
\(|\xi_x|^2|\xi_y|^2\)，在 \(\xi_x=0,\xi_y\ne0\) 或反之时消失，故不满足四阶椭圆性。

---

## 3. 被引结果核对

### 3.1 Hardy–Wright, Theorem 278

应固定版本为：G. H. Hardy and E. M. Wright, revised by D. R. Heath-Brown and
J. H. Silverman, *An Introduction to the Theory of Numbers*, 6th ed., Oxford
University Press, 2008, **Theorem 278**。该定理对应二平方表示数公式/判据，支持

\[
r_2(k)=4\bigl(d_1(k)-d_3(k)\bigr)
=4\sum_{\substack{d\mid k\\ d\ \mathrm{odd}}}(-1)^{(d-1)/2},\qquad k\ge1.
\]

它不是所写圆盘计数误差 \(B(K)=\pi K+O(K^{1/2})\) 的精确定位。因此原稿
把 Hardy–Wright, Thm 278 同时列作 Gauss 圆盘估计的直接出处并不准确。
第六版书目信息可由 [Oxford/Google Books 条目](https://books.google.de/books?id=P6uTBqOa3T4C)
核对；较早版本的公开书目元数据见
[Internet Archive 条目](https://archive.org/details/introductiontoth0000hard)。

### 3.2 Ivić, §12.1

A. Ivić, *The Riemann Zeta-Function*, Wiley, 1985（Dover 2003 重印）的第 12 章是
“The Distribution of Primes”，所以 §12.1 不是 Gauss 圆问题的正确定位。
该书目录把 “The Circle Problem” 列在第 13 章范围内、约第 372 页；参见
[Google Books 目录](https://books.google.com/books/about/The_Riemann_Zeta_Function.html?id=tUXCAgAAQBAJ)。
建议引用为“Chapter 13, ‘The Circle Problem’, p. 372”，并注明所用版本，而不要写
§12.1。

### 3.3 本证明其实无需把圆盘粗界作为黑箱

令 \(R=\sqrt K\)，并以每个 \(p\in\mathbb Z^2\) 为中心放置边长 \(1\) 的单位方格。
这些方格内部互不相交。设 \(c=\sqrt2/2\)，则

\[
D_{R-c}\subseteq
\bigcup_{|p|\le R}\left(p+[-\tfrac12,\tfrac12]^2\right)
\subseteq D_{R+c}.
\]

取面积即得（\(K\ge1\)）

\[
\pi(R-c)^2\le B(K)\le\pi(R+c)^2,
\]

从而例如

\[
|B(K)-\pi K|\le \pi\sqrt{2K}+\frac\pi2.
\]

因此本件实际所需的 \(O(K^{1/2})\) 是初等几何结论，既不需要圆问题的深结果，
也不需要任何关于 \(\zeta\) 的输入。

---

## 4. Step 1：降为对 \(p\) 的求和

定义

\[
A(X)=\#\{q\in\mathbb Z^2:1+|q|^2\le X\},\qquad X\ge1.
\]

固定 \(p\) 后，允许的 \(q\) 恰由
\(1+|q|^2\le\Lambda/(1+|p|^2)\) 给出，所以

\[
N_{H_{\mathrm{prod}}}(\Lambda)
=\sum_{1+|p|^2\le\Lambda}
A\!\left(\frac{\Lambda}{1+|p|^2}\right).
\]

由上一节的圆盘粗界，对所有 \(X\ge1\) 可写

\[
A(X)=\pi X+\varepsilon(X),\qquad
|\varepsilon(X)|\le C X^{1/2}
\]

（\(\pi(X-1)\) 与 \(\pi X\) 相差的常数 \(-\pi\) 可统一吸收）。应把余项严格定义为

\[
R(\Lambda):=
\sum_{1+|p|^2\le\Lambda}
\varepsilon\!\left(\frac{\Lambda}{1+|p|^2}\right),
\]

而不是把 \(R\) 定义为“若干 \(O(\cdot)\) 的和”。于是

\[
N_{H_{\mathrm{prod}}}(\Lambda)
=\pi\Lambda S_1(\Lambda)+R(\Lambda),
\qquad
S_1(\Lambda)=\sum_{1+|p|^2\le\Lambda}\frac1{1+|p|^2}.
\]

这是精确恒等式。有限求和与统一误差估计的交换没有问题。

**Step 1：CONFIRMED，需作上述记号性严化。**

---

## 5. Step 2：Abel 求和及正确边界项

令

\[
B(k)=\sum_{j=0}^{k}r_2(j),\qquad
E(k)=B(k)-\pi k.
\]

注意 \(E(0)=B(0)=1\)；只有对 \(k\ge1\) 才可直接写
\(E(k)=O(k^{1/2})\)。有限 Abel 求和给出

\[
S_1(\Lambda)
=\frac{B(N-1)}N
+\sum_{k=0}^{N-2}\frac{B(k)}{(k+1)(k+2)}. \tag{5.1}
\]

原稿的这个公式本身正确。问题出现在下一行：第二项的主部应只求到 \(N-2\)，
不能写成 \(N-1\)。对 \(N\ge2\)，

\[
\frac{k}{(k+1)(k+2)}=-\frac1{k+1}+\frac2{k+2},
\]

且

\[
\sum_{k=1}^{N-2}\frac{k}{(k+1)(k+2)}
=H_{N-1}+\frac2N-2.
\]

把 (5.1) 中 \(B(N-1)/N\) 的主部一起合并，恰得

\[
\pi\left(\frac{N-1}{N}
+\sum_{k=1}^{N-2}\frac{k}{(k+1)(k+2)}\right)
=\pi(H_N-1). \tag{5.2}
\]

因此完全正确的恒等式是

\[
S_1(\Lambda)
=\pi(H_N-1)
+\frac{E(N-1)}N
+\sum_{k=0}^{N-2}\frac{E(k)}{(k+1)(k+2)}. \tag{5.3}
\]

由于

\[
\sum_{k=1}^{\infty}
\frac{|E(k)|}{(k+1)(k+2)}<\infty,
\]

可以给出精确常数

\[
c_0=\pi(\gamma-1)
+\sum_{k=0}^{\infty}
\frac{B(k)-\pi k}{(k+1)(k+2)}. \tag{5.4}
\]

由 \(H_N=\log N+\gamma+O(N^{-1})\)、边界项
\(E(N-1)/N=O(N^{-1/2})\) 及收敛级数尾部估计，得到

\[
S_1(\Lambda)=\pi\log N+c_0+O(N^{-1/2})
=\pi\log\Lambda+c_0+O(\Lambda^{-1/2}). \tag{5.5}
\]

这比主定理所需的 \(\pi\log\Lambda+O(1)\) 更精确。

原稿中的

\[
\pi\left(\log N-1-\frac12+O(1/N)\right)
\]

不是正确的常数级展开：即便采用原稿错误的上限 \(N-1\)，也会出现
\(\gamma\)。若只保留“\(=\pi\log N+O(1)\)”则结论仍正确。

此外，仅从所给 \(E(k)=O(k^{1/2})\) 不能推出题目建议的
\(O((\log\Lambda)/\Lambda)\) 收敛率；由该输入直接得到的是 (5.5) 的
\(O(\Lambda^{-1/2})\)。这不影响主定理。作为可选数值核对，Poisson 求和还给出

\[
c_0=2\pi\sum_{m\in\mathbb Z^2\setminus\{0\}}K_0(2\pi|m|)
\approx0.0245228700569348,
\]

但此特殊函数表示不参与证明链。

**Step 2：主结论 CONFIRMED；原显示推导需按 (5.1)–(5.5) 替换。**

---

## 6. Step 3：余项 \(R(\Lambda)=O(\Lambda)\)

由 Step 1 的统一估计，

\[
|R(\Lambda)|
\le C\Lambda^{1/2}
\sum_{k=0}^{N-1}r_2(k)(1+k)^{-1/2}
=C\Lambda^{1/2}T(\Lambda). \tag{6.1}
\]

把 \(k=0\) 单独取出。对 \(j\ge1\)，令

\[
I_j=\{k:2^{j-1}<k\le\min(2^j,N-1)\},
\]

并令 \(j\) 取到 \(J=\lceil\log_2(N-1)\rceil\)（空壳忽略）。在 \(I_j\) 上，

\[
(1+k)^{-1/2}\le C_1 2^{-j/2},
\qquad
\sum_{k\in I_j}r_2(k)\le B(2^j)=O(2^j).
\]

故

\[
\sum_{k\in I_j}r_2(k)(1+k)^{-1/2}=O(2^{j/2}),
\]

并且

\[
T(\Lambda)
\le1+\sum_{j=1}^{J}O(2^{j/2})
=O(2^{J/2})=O(N^{1/2})=O(\Lambda^{1/2}). \tag{6.2}
\]

代回 (6.1) 即得

\[
R(\Lambda)=O(\Lambda).
\]

原稿的思路正确，但 \(I_0\) 的定义没有覆盖 \(k=0\)，而
\(J=\lfloor\log_2N\rfloor\) 在 \(N\) 非二次幂时可能漏掉最后一段；以上定义修复了两点。

**Step 3：CONFIRMED，需修正壳层端点。**

---

## 7. Step 4：合并

由 (5.5) 与 Step 3，

\[
\begin{aligned}
N_{H_{\mathrm{prod}}}(\Lambda)
&=\pi\Lambda
\bigl(\pi\log\Lambda+c_0+O(\Lambda^{-1/2})\bigr)
+O(\Lambda)\\
&=\pi^2\Lambda\log\Lambda+O(\Lambda).
\end{aligned}
\]

\(\pi^2\) 的来源核对无误：一个 \(\pi\) 来自二维圆盘面积，另一个 \(\pi\)
来自加权格点调和和。项 \(\pi c_0\Lambda\) 被 \(O(\Lambda)\) 吸收。

**Step 4：CONFIRMED。**

---

## 8. 独立数值核验

### 8.1 两条路线

下列标准库程序同时使用：

1. 直接枚举四个整数坐标；
2. 独立按 Jacobi 除数公式计算 \(r_2(k)\)，再作范数卷积。

两条路线均只用整数决定是否计数。

~~~python
from math import isqrt

def direct(L):
    m = isqrt(L - 1)
    vals = [1 + a*a + b*b
            for a in range(-m, m + 1)
            for b in range(-m, m + 1)
            if 1 + a*a + b*b <= L]
    return sum(x*y <= L for x in vals for y in vals)

def jacobi_r2(k):
    if k == 0:
        return 1
    s = 0
    for d in range(1, isqrt(k) + 1):
        if k % d:
            continue
        divisors = (d,) if d*d == k else (d, k//d)
        for e in divisors:
            if e % 2:
                s += 1 if e % 4 == 1 else -1
    return 4*s

def norm_sum(L):
    r = [jacobi_r2(k) for k in range(L)]
    B, total = [], 0
    for v in r:
        total += v
        B.append(total)
    return sum(r[k] * B[L//(k + 1) - 1] for k in range(L))

for L in (10, 100):
    a, b = direct(L), norm_sum(L)
    print(L, a, b, a == b)
~~~

真实运行输出：

~~~text
10 153 153 True
100 3505 3505 True
~~~

### 8.2 锚点结论

原稿的 \(N(10)=153\) **完全正确**。

对 \(\Lambda=100\)，独立精确值为

\[
\boxed{N_{H_{\mathrm{prod}}}(100)=3505}.
\]

主项及误差为

\[
\pi^2\,100\log100\approx4545.12079353936,
\]

\[
N(100)-\pi^2\,100\log100\approx-1040.12079353936,
\]

相对误差

\[
\frac{N(100)-\pi^2\,100\log100}
{\pi^2\,100\log100}
\approx-0.2288433775=-22.88433775\%.
\]

这与渐近定理不冲突；但它略大于原稿启发式写出的 \(1/\log100\approx21.7\%\)，
且绝对误差并非“至多 \(100\)”。由于 \(O(\Lambda)\) 未指定隐含常数，
单个 \(\Lambda=100\) 数据点既不能验证也不能反驳该误差阶。它只能作为程序一致性检查。

---

## 9. 升级为 GATE-A PASS 所需的确切修改

1. **Step 1：** 将 \(R(\Lambda)=\sum O(\cdot)\) 改为先定义
   \(\varepsilon(X)=A(X)-\pi X\)，再令
   \(R(\Lambda)=\sum_p\varepsilon(\Lambda/(1+|p|^2))\)。
2. **Step 2：** 用本报告 (5.1)–(5.5) 整段替换原 Abel 主项计算；特别把
   \(\sum_{k=1}^{N-1}\) 改为 \(\sum_{k=1}^{N-2}\)，并与边界项合并成
   \(\pi(H_N-1)\)。
3. **\(k=0\)：** 明写 \(E(0)=1\)，误差级数中把 \(k=0\) 单独处理，禁止写
   \(B(0)=O(0^{1/2})\)。
4. **常数项：** 删除
   \(\log N-1-1/2+O(1/N)\)；若需要精确常数，采用 (5.4)，并把由当前输入
   可证的余项写为 \(O(\Lambda^{-1/2})\)，不得声称已证
   \(O((\log\Lambda)/\Lambda)\)。
5. **Step 3：** 单列 \(k=0\)，并用
   \(J=\lceil\log_2(N-1)\rceil\) 或显式添加最后一个不完整壳。
6. **书目：** 将 Hardy–Wright Theorem 278 只用于 Jacobi 二平方表示公式；
   删除 Ivić §12.1，改成带版本的 Chapter 13 / “The Circle Problem” / p. 372，
   或直接采用第 3.3 节的初等面积证明而不引用圆问题文献。
7. **数值段：** 加入精确值 \(N(100)=3505\) 与相对误差
   \(-22.88433775\%\)；删除“\(O(100)\) 即绝对误差约不超过 \(100\)”及
   “相对误差应不超过 \(1/\log100\)”的解释。
8. **Lint 状态：** 将 L17 从 PASS 改为 CONDITIONAL，直至书目定位完成修订；
   L18 在加入 \(N(100)\) 的双路线复算后方可记 PASS。

---

## 10. Gate-A 问题逐项回答

| 问题 | 独立判断 |
|---|---|
| 各环节能否连成完整证明？ | 能，但 Step 2 和 Step 3 必须采用本报告的端点修正。修正后 Step 1 \(\to\) Step 2/3 \(\to\) Step 4 输入输出完全衔接。 |
| 是否有隐藏分析间隙？ | 无致命间隙；有 off-by-one、\(k=0\)、尾壳和常数项错误，均为局部可修复。 |
| 是否非平凡？ | 是。两条独立整数算法给出 \(N(10)=153\)、\(N(100)=3505\)，且扰动计数条件会改变结果。 |
| 解析步骤与有限步骤是否分离？ | 是。解析输入是统一圆盘误差及 Abel 求和；数值锚点只作 sanity check，不参与渐近证明。 |
| 范围与“逃逸”声明是否诚实？ | 是。该算子四阶但非椭圆，\(\Lambda\log\Lambda\) 增长确使其落在四维四阶椭圆 Weyl 类之外。 |
| 是否存在 RH 或 \(\zeta\) 零点输入？ | **不存在。** 全链只涉及有限格点、圆盘面积界、调和和与有限求和。 |
| 最终状态 | **GATE-A CONDITIONAL**；完成第 9 节八项文字修订后为 **GATE-A PASS**。 |

## 11. 可在修订稿中采用的结论句

> \(N_{H_{\mathrm{prod}}}(\Lambda)=\pi^2\Lambda\log\Lambda+O(\Lambda)\)，
> 由二维格点圆盘粗界和 Abel 求和推出；证明不使用 RH、\(\zeta\) 零点或任何
> 与 RH 等价的陈述。当前独立核验的精确锚点为 \(N(10)=153\) 和
> \(N(100)=3505\)。

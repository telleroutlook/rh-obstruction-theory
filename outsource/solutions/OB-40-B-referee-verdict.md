# OB-40-B 独立审稿报告：Seeley 复幂与 \(H^{1/m}\) 的经典符号

**数学裁决：`CONFIRMED`**  
**Gate-A 裁决：`GATE-A CONDITIONAL`**

条件不是数学缺口：Paper B 所需的降阶论证成立。条件来自送审文本中两处必须先修正的事实性表述，以及 Paper B 引文需要补到可独立核查的精度。完成第 7 节列出的文字修改后，本件可改判为 `GATE-A PASS`。

## 1. 逐项结论

| 项目 | 独立结论 | 理由 |
|---|---|---|
| Claim A：存在性 | **成立** | 正自伴严格正的 \(H\) 有正谱函数演算；选负实轴为谱割后，Seeley–Shubin 复幂演算把该谱幂识别为伪微分算子。 |
| Claim B：经典性 | **成立** | 若 \(H\in\Psi^m_{\mathrm{cl}}(M)\)，则 \(H^z\in\Psi^{mz}_{\mathrm{cl}}(M)\)，符号按次数 \(mz-j\) 多齐次展开，首项为 \(h_m^z\)。取 \(z=1/m\) 即得 \(H^{1/m}\in\Psi^1_{\mathrm{cl}}(M)\) 与 \(\sigma_1(H^{1/m})=h_m^{1/m}\)。 |
| Claim C：Weyl 律所需条件 | **需区分** | 完整经典展开不是首项 Weyl 律的逻辑最小条件；Hörmander 1968 的框架允许一般 \(S^1_{1,0}\) 符号，但仍要求存在正的次数 1 齐次主极限。仅说“任意一阶椭圆 \(S^1_{1,0}\) 算子”则不够。 |
| Claim D：计数降阶 | **成立** | 谱函数演算保持本征向量与重数，特征值变为 \(e_k^{1/m}\)，故计数恒等式及相空间常数完全一致。 |

这里按附件公式理解 \(H\) 为标量算子（或作用于秩一丛）。若 Paper B 允许高秩向量丛，Weyl 常数必须改为对主符号各本征值的指标函数取纤维迹；这不影响降阶原理，但应在定理假设中说清。

## 2. Claim A–B：Seeley 构造确实给出经典复幂

### 2.1 精确的可核查结果

可直接采用的带编号引文是：

> M. A. Shubin, *Pseudodifferential Operators and Spectral Theory*, 2nd ed., Springer, 2001, **§11, Theorem 11.2**（不是附件所写的 §9）。

[Springer 的章节目录](https://link.springer.com/chapter/10.1007/978-3-642-56579-3_2)显示该章为 “Complex Powers of Elliptic Operators”，其中 §9 是带参数的预解式，§10 是复幂的定义与基本性质，§11 才是复幂的结构。Theorem 11.2 在避开所选谱割的经典椭圆算子上给出复幂的伪微分结构；对本件的正自伴 \(H\)，负实轴满足谱割条件。其结论在当前记号下为

\[
H^z\in\Psi^{mz}_{\mathrm{cl}}(M),\qquad
\sigma(H^z)(x,\xi)\sim\sum_{j=0}^{\infty}h_{mz-j}^{(z)}(x,\xi),
\]

其中 \(h_{mz-j}^{(z)}\) 对 \(\xi\) 正齐次于次数 \(mz-j\)，且

\[
h_{mz}^{(z)}(x,\xi)=h_m(x,\xi)^z
\]

（沿所选谱割取支）。Werner Müller 在应用中明确以 “[Seeley], [Shubin, Theorem 11.2]” 得出平方根是**经典**伪微分算子，并写出次数 \(1-j\) 的完整齐次展开；见其论文 [§2，公式 (2.8)–(2.9)](https://www.math.uni-bonn.de/people/mueller/papers/selberg.pdf)。

Seeley 1967 原文没有把所需全部结论包装成一个方便引用的单一编号定理，因此不应虚构 “Seeley, Theorem X”。其构造的关键恰是带参数的**经典**预解式：若

\[
q(x,\xi;\lambda)\sim\sum_{j\ge 0}q_{-m-j}(x,\xi;\lambda),
\]

各项对 \((\xi,\lambda^{1/m})\) 具有相应齐次性，则逐项作轮廓积分产生次数 \(mz-j\) 的项。Ponge 对 Seeley 原始论证的逐式回顾清楚写出了这个过程及最终多齐次展开，见 [Ponge, §2](https://arxiv.org/pdf/math/0601529)。因此附件所谓“Seeley 只落在较宽的非经典 \(S^m_{1,0}\) 演算”的 gap 描述不正确：\(S^{mz}_{1,0}\) 估计只是经典符号同时满足的较弱外层估计，并不是该构造的最终精度。

### 2.2 与谱论定义的一致性

对 \(\operatorname{Re}z<0\)，沿负实轴割线的全纯函数演算给出轮廓积分；它与正自伴算子的谱演算一致。其余 \(z\) 由整数移位（或乘以 \(H^k\)）延拓。因此这里不是先构造一个名字相同但可能不同的伪微分算子：所得算子就是谱论意义的 \(H^z\)。严格正性 \(H>0\) 排除了零点处分支和逆幂的额外约定。

### 2.3 附件轮廓公式的符号问题

附件写成

\[
\frac{i}{2\pi}\int_\Gamma \lambda^z(\lambda-H)^{-1}\,d\lambda
\]

但没有指定 \(\Gamma\) 的方向；这会留下一个整体符号歧义。应任选一种自洽写法：

\[
H^z=\frac{i}{2\pi}\int_{\Gamma}\lambda^z(H-\lambda)^{-1}\,d\lambda
\]

并采用 Seeley 的轮廓方向；或使用标准正向闭合轮廓写成

\[
H^z=\frac{1}{2\pi i}\int_{\Gamma}\lambda^z(\lambda-H)^{-1}\,d\lambda.
\]

该问题不改变结论，但送审件必须补方向或改系数，不能把目前的式子当作无条件精确陈述。

## 3. Claim C：完整经典性不是最小条件，但任意 \(S^1_{1,0}\) 椭圆性不够

Hörmander 的原始结果并不要求符号有全部次数 \(1,0,-1,\ldots\) 的经典展开。其 [1968 年论文 §3 与 Theorem 4.4](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6063-11511_2006_Article_BF02391913.pdf)处理一阶、自伴、半有界、\((1,0)\) 型椭圆算子，并使用存在且为正的齐次主极限

\[
a_1(x,\xi)=\lim_{t\to\infty}t^{-1}a(x,t\xi)>0.
\]

其对角谱函数首项积分后给出

\[
N_A(\Lambda)=(2\pi)^{-d}
  \operatorname{vol}\{(x,\xi):a_1(x,\xi)\le 1\}\,\Lambda^d
  +o(\Lambda^d).
\]

同一论文 Theorem 5.1 的证明还明确令 \(A=P^{1/m}\)，并援引 Seeley 说明其符号由 \(p^{1/m}\) 与次数 \(0,-1,-2,\ldots\) 的齐次项渐近组成，然后应用 Theorem 4.4。这直接覆盖 Paper B 的用法。

但“属于 \(S^1_{1,0}\) 且椭圆”本身并不保证上述主极限，更不保证一个固定 Weyl 常数。一个明确反例是平坦环面 \(\mathbb T^d\) 上的正 Fourier 乘子，在大 \(|\xi|\) 处取

\[
a(\xi)=\langle\xi\rangle
\left(2+\tfrac12\sin\log\langle\xi\rangle\right).
\]

它是正的、椭圆的 \(S^1_{1,0}\) 符号；径向函数的导数为

\[
2+\tfrac12(\sin t+\cos t)>0,
\]

故大半径处严格递增。然而 \(t^{-1}a(t\xi)\) 因 \(\sin(\log t+\log|\xi|)\) 振荡而没有极限。若 \(\Lambda_R=R(2+\tfrac12\sin\log R)\)，格点计数给出

\[
\frac{N_A(\Lambda_R)}{\Lambda_R^d}
\sim
\frac{\omega_d}{(2+\tfrac12\sin\log R)^d},
\]

右侧沿 \(\log R=\pi/2+2\pi n\) 与 \(3\pi/2+2\pi n\) 有不同极限。因此一般 \(S^1_{1,0}\) 椭圆性不足以推出 \(N_A(\Lambda)\sim C\Lambda^d\)。

结论是：Paper B 可以使用较弱于“完整经典”的 Hörmander 假设，但不能把它进一步削弱成任意 \(S^1_{1,0}\) 椭圆算子。当前对象由 Seeley–Shubin 定理本来就是经典的，所以这一边界问题不形成证明缺口。

## 4. Claim D：计数恒等式与 Weyl 常数

设 \(He_k=e_ke_k\)，并按重数排列 \(e_k>0\)。谱函数演算给出

\[
H^{1/m}e_k=e_k^{1/m}e_k.
\]

因此，对相同的 \(\le\) 计数约定，逐个特征值即有精确恒等式

\[
N_{H^{1/m}}(t)=N_H(t^m),
\qquad
N_H(\Lambda)=N_{H^{1/m}}(\Lambda^{1/m}).
\]

若令 \(B=H^{1/m}\)，则 \(b_1=h_m^{1/m}\)，所以

\[
\begin{aligned}
N_B(t)&\sim C_Bt^d,\\
C_B&=(2\pi)^{-d}\int_{T^*M}\mathbf 1_{\{b_1\le1\}}\,dx\,d\xi\\
&=(2\pi)^{-d}\int_{T^*M}\mathbf 1_{\{h_m\le1\}}\,dx\,d\xi>0.
\end{aligned}
\]

代入 \(t=\Lambda^{1/m}\) 得

\[
N_H(\Lambda)\sim C_B\Lambda^{d/m}.
\]

这里的第二个集合等式使用 \(h_m>0\) 与正实根的单调性；没有额外渐近误差，也没有丢失重数。

## 5. 数值锚点的独立精确核验

用纯整数与 `fractions.Fraction` 脚本独立计算得到：

```text
{'N_H(100)': 19, 'N_Hsqrt(10)': 19, 'modes': [-9, 9], 'weyl_constant_exact': '2'}
```

具体地，\(n^2+1\le100\iff |n|\le9\)，故两个计数均为 \(19\)。主符号是 \(h_2(x,\xi)=\xi^2\)，不是 \(\xi^2+1\)；精确约去 \(\pi\) 后

\[
C_H=(2\pi)^{-1}(2\pi)\operatorname{vol}[-1,1]=2.
\]

附件数值锚点中先后出现的 \(0\)、\(2/\pi\)、\(1/\pi\) 都是错误中间值；最后的 \(2\) 才正确。发布版本应删除整段错误试算，只保留正确计算，以免形成互相矛盾的陈述。

## 6. 证明链与非循环性审计

证明链闭合如下：

1. 正自伴谱演算定义 \(H^{1/m}\)，保持特征向量和重数；
2. Shubin §11, Theorem 11.2（Seeley 构造）给出 \(H^{1/m}\in\Psi^1_{\mathrm{cl}}\) 及主符号 \(h_m^{1/m}\)；
3. Hörmander 1968, Theorem 4.4 给出该一阶算子的 Weyl 首项；
4. 精确计数恒等式把该首项改写为 \(H\) 的 \(\Lambda^{d/m}\) Weyl 律。

每一步的输出恰好满足下一步的输入。整条链只使用谱函数演算、参数伪微分演算、相空间体积与特征值单调变换；没有假设 RH、RH 等价命题、\(\zeta\) 零点位置、Euler 乘积或零点计数律。故非循环性检查通过。

## 7. `GATE-A CONDITIONAL` 所需的确切文字修改

### 7.1 Paper B 的建议替换句

把原括号说明替换为：

> For general \(m>0\), let \(B=H^{1/m}\) by the positive spectral calculus. By Shubin (2001), §11, Theorem 11.2 (Seeley’s complex-powers construction), \(B\in\Psi^1_{\mathrm{cl}}(M)\) is positive elliptic and \(\sigma_1(B)=h_m^{1/m}\). Hence Hörmander (1968), Theorem 4.4 applies, and \(N_H(\Lambda)=N_B(\Lambda^{1/m})\).

### 7.2 送审件本身的必要修订

1. 把 “The gap” 段改为：Seeley 构造位于带参数的经典演算中，并产生完整多齐次展开；一般 \(S^{mz}_{1,0}\) 归属只是其较弱推论。
2. 把候选引文 “Shubin §9” 改为 **Shubin §11, Theorem 11.2**；可说明 §9 只负责带参数预解式。
3. 按第 2.3 节修正轮廓公式的预解式符号/系数，并明确轮廓方向与谱割。
4. 删除数值锚点中 \(0\)、\(2/\pi\)、\(1/\pi\) 三个错误常数，只保留 \(C_H=2\)。
5. 明确算子是标量的；若允许向量丛，则把 Weyl 常数写成纤维迹版本。

完成上述修改后，Paper B 的该段降阶证明可标记为 `INDEPENDENTLY-CHECKED`，本裁决随之升级为 **`GATE-A PASS`**。

## 8. 参考文献定位

- R. T. Seeley, “Complex powers of an elliptic operator,” *Proc. Sympos. Pure Math.* 10 (1967), 288–307；[AMS 卷目录](https://www.ams.org/books/pspum/010/pspum010-endmatter.pdf)。
- M. A. Shubin, *Pseudodifferential Operators and Spectral Theory*, 2nd ed., Springer, 2001, **§11, Theorem 11.2**；[Springer 章节页](https://link.springer.com/chapter/10.1007/978-3-642-56579-3_2)。
- L. Hörmander, “The spectral function of an elliptic operator,” *Acta Math.* 121 (1968), 193–218, **Theorems 4.4 and 5.1**；[原文 PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6063-11511_2006_Article_BF02391913.pdf)。
- R. Ponge, “Functional calculus and spectral asymptotics for hypoelliptic operators on Heisenberg manifolds I,” §2 对 Seeley 构造的回顾；[arXiv PDF](https://arxiv.org/pdf/math/0601529)。


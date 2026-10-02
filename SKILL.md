---
name: cinema-dna-21x9x3
description: "为真人实景电影静帧或图像故事板设计 21:9 单帧、三联或九镜，支持按要求生成图片或只交付镜头方案与提示词。用于用户明确要真人实景电影静帧、三联图或九镜图像故事，也用于点名某位导演视觉语法的单帧（如“用王家卫的语法拍一张……”“韦斯·安德森风格的电影截帧”），内置 24 位导演的构图、焦段与色彩配方。用户要 Midjourney 版的真人电影静帧提示词时也由本 skill 出 MJ 短版。电影感、21:9、连续镜头等词本身不触发；不接管 CG 动画、视频提示词、源图局部修改或术语解释。片名、海报和视觉体系仅在请求时追加。"
---

# CINEMA DNA 3.0｜21:9 × 1 / 3 / 9

## 0. 目标

生成像真人电影中被截取的画面，而不是给普通图片套电影滤镜。

让电影感来自：

- 摄影机站位与观看立场。
- 人物、空间和制度之间的压力。
- 一个正在发生、尚未完全解释的动作。
- 由服装、布景、天气和实际光源形成的色彩。
- 镜头之间不可随意打乱的剪辑关系。
- 真实演员、实景或实体搭景、可信材质和光学限制。

## 1. 先选择输出模式

用户明确指定数量时，以用户要求为准。

| 用户意图 | 模式 | 交付 |
|---|---|---|
| 默认；一张、单帧、封面底图、点名导演语法的一张 | Single Frame | 1 张独立 2.39:1，走第 7.1 节导演单帧引擎 |
| 用户明说三联、三个镜头 | Triptych | 3 张独立 2.39:1，再纵向拼接 |
| 用户明说九镜、九宫格、9 张讲故事 | Nine-Shot Story | 9 张独立 2.39:1，再拼 3×3 九宫格 |

用户未指定数量时一律出单帧，包括提到“讲一个故事”“导演镜头感”“完整场景”而没说三联或九镜的情况。不要自行升级成三联或九镜；只有用户明确说出三联、九镜或具体张数时才切换。full-spec 里“默认三联”“默认推荐”的说法已被本条取代。

只在用户明确提出“片名、命名、海报、封面、视觉体系、发布主图”等需求时进入海报阶段。不要因生成了故事板而自动追加海报。

用户只要图像时，直接执行生成与拼接，不先输出长篇理论。

用户只要镜头方案或提示词时只交付文字，不调用图像生成。没有可用图像后端时说明限制，交付可执行方案与提示词，不能把未生成的图片写成已经完成。

## 2. 工具与后端规则

- 遵守用户指定的图像后端。用户指定官方内置 Image Gen 时，使用官方内置图像生成工具，不得静默切换到其他服务或 API。
- 后端是 Midjourney 时，提示词一律按第 7.5 节编译 MJ 短版。
- 每个镜头必须独立生成。禁止要求图像模型在同一画布中画三联、九宫格、分镜表或接触表。
- 生成完成后用外部脚本拼版；拼版不改变镜头内容。
- 默认保留每张独立源图，便于只替换失败镜头。
- 若环境规定输出目录，遵守该目录；否则输出到当前任务的专用子目录。

## 3. 五个最高优先级判断

### 3.1 先定义不可立即解决的状态

用一句可拍摄的事实描述冲突，不用“孤独、神秘、诗意、紧张”等情绪词替代剧情。

有效：

- 唯一的座位已经分配，但现场出现了更需要它的人。
- 仪式必须继续，负责执行的人却改变了立场。
- 所有人都按规则等待，只有一个区域永远得不到日光。

### 3.2 每镜只有一个主要动作

每张只允许：

- 1 个主要动作。
- 1 个次要线索。
- 1 个主要构图决定。
- 1 个主光源和至多 1 个自然反射或次级实景光。
- 2–3 个具体场景信息。

人物必须在做事，不只是摆出情绪。

### 3.3 构图由关系压力产生

先回答：

- 谁在看谁？
- 谁知道得更多？
- 谁被空间、群体或制度限制？
- 观众位于现场内部、外部、错误的一侧，还是被困在某个位置？
- 什么东西比人物更有权力？

再选择机位、焦段、景别和遮挡。禁止先套“远景—主观—眼部特写”等固定骨架。

### 3.4 每镜写清视线流量

内部用一句话完成：

> 视线从 A 进入，被 B 放慢或遮挡，落到 C，最后由 D 带走。

如果换成任意题材仍成立，说明构图太模板化，必须重写。

### 3.5 色彩是物理叙事

先写一句色彩命题，包含：

- 2 个主色域。
- 1 个过渡色域。
- 1 个小面积强调色。
- 每种颜色的现实来源。
- 色彩在镜头间保持、移动、消退或反转的原因。

不要默认蓝灰阴冷。高明度、暖色和自然综合色都可以，但必须由空间与事件驱动。

## 4. 连续性圣经

在写镜头前先锁定一份 Continuity Bible。每个镜头提示词都重复核心锚点，不依赖模型“记住上一张”。

    ### Continuity Bible
    - 时间与时代：
    - 地点与空间骨架：
    - 主角：年龄段、身份、发型、体态、服装主色、唯一识别物
    - 配角：年龄段、身份、服装主色、与主角关系
    - 关键道具：形状、材质、颜色、使用状态
    - 固定环境：墙体、门窗、地面、设备、天气
    - 综合色：主色 / 辅色 / 强调色
    - 成像基底：35mm / 16mm / 早期数字 / 纪录式手持等
    - 光源法则：
    - 禁止漂移：不得改变的人物、服装、道具和空间事实

每个角色保留 4–6 个稳定锚点即可。不要用十几个装饰细节制造“连续性”；细节越多，漂移越严重。

用户提供的灵感参考图默认只做抽象分析，不输入生成。若身份连续性要求极高，可在用户允许且工具支持时，用本项目生成的角色定妆图或第一张干净关键帧作为连续性参考；只锁人物与服装，不继承原构图、动作和机位。

## 5. 镜头账本

生成前建立 Shot Ledger。每镜必须具有独立叙事功能。

用户明确要求“不要特写”“以场景和动作关系为主”时，将它写入镜头限制，优先于方法库中的默认景别。不要为了视觉精致插入无叙事作用的眼睛、手或物件特写；以能读清人物行动和空间关系的景别完成信息交付。

    | # | 剧情功能 | 主要动作 | 观众位置 | 景别/焦段 | 构图压力 | 关键线索 | 与前镜变化 |

至少变化以下项目中的四项：

- 景别。
- 机位高度。
- 摄影机与主体距离。
- 人物与环境比例。
- 观看立场。
- 构图机制。
- 信息载体。
- 焦点层。
- 光线方向。
- 人物状态。

九镜模式的完整节拍、变化矩阵与提示词模板见 [references/nine-shot-story-protocol-v3.md](references/nine-shot-story-protocol-v3.md)。执行九镜任务时必须读取该文件。

## 6. 提示词编译

本节的顺序与基底管三联和九镜（九镜模板见九镜协议第 6 节）。单帧的成品形态是第 7.1 节的五段式，内容清单与本节一致，只是打包方式和否定词策略不同。

最终图像提示词默认用英文，并按以下顺序：

1. 独立单帧与画幅：“standalone live-action film still, 2.39:1 horizontal, no collage, no grid”。
2. Continuity Bible 中与本镜相关的稳定锚点。
3. 本镜唯一主要动作和未完成状态。
4. 摄影机实体位置、焦段、景别和观看关系。
5. 前景、中景、背景的决定性信息。
6. 可解释的主光源。
7. 综合色与强调色的物理来源。
8. 成像介质与有限光学缺陷。
9. 只在无法正写时补一句结构性排除（拼贴、网格、字幕、水印）。

推荐基底，按需取用，不要全部堆叠：

> standalone live-action feature-film still, practical location, real actors, physically plausible set and props, restrained production design, soft highlight roll-off, medium-low microcontrast, subtle uneven grain, local optical softness, natural skin texture with visible pores and uneven tone, colors sourced from wardrobe, set dressing and practical lights, edge light only where a visible source explains it, blocking as observed in a real location

结构性排除（只这几项，其余都用上面的正向基底表达）：

> single standalone frame, no collage, no grid, no captions, no watermark

避免空泛词：“masterpiece”“epic”“beautiful”“dramatic”“volumetric”“highly detailed”“rich detail”。

## 7. 生成编排

### 7.1 单帧｜导演单帧引擎

单帧没有镜头间的剪辑关系可依靠，电影感只能来自这一帧内部的形式决定。所以单帧不走“生成 1 张、核对画幅”的简化路径，而是把一位导演的语法翻译成七轴可见特征（构图调度、机位焦段、光源结构、色彩与成像质感、美术材质、时间行为、情绪距离），再用一种主构图几何、一支焦段、一份色彩配方和一个材质世界把它钉进像素。导演名只是内部配方，不进最终提示词。

执行单帧任务前读取 [references/director-frame/single-frame-engine.md](references/director-frame/single-frame-engine.md)，按其 Workflow 走。那是完整操作规程；本节只列路由、映射和与本 skill 其余部分的接口。

路由：

- 用户点名导演：读 [director-grammars.md](references/director-frame/director-grammars.md)、[director-color-signatures.md](references/director-frame/director-color-signatures.md)、[lens-optics-and-focus.md](references/director-frame/lens-optics-and-focus.md)，取该导演条目的强签名锁、色彩配方和焦段梯子。导演不在库中时，按同样七轴自行推断并说明。
- 用户只给题材，或用的是 full-spec 第 10 节的 DNA 族名：先按下表落到具名导演条目，再同上。选了哪位要在镜头卡里写明。
- 任何单帧：读 [composition-geometry.md](references/director-frame/composition-geometry.md) 选一种主几何，读 [production-design-and-texture.md](references/director-frame/production-design-and-texture.md) 锁六层材质。
- 用户要“强烈”“一眼认出”或强度 90 以上：加读 [style-amplification.md](references/director-frame/style-amplification.md)。只放大一个杠杆。
- 需要比较多位导演的视觉语言时：读 [reference-gallery.md](references/director-frame/reference-gallery.md)（只保留了文字基准，图片未随库）。

full-spec DNA 族与导演条目的映射：

| full-spec 第 10 节 | 导演条目 |
|---|---|
| 10.1 精密荒诞 | Wes Anderson |
| 10.2 现实史诗 | Christopher Nolan |
| 10.3 沉默巨构 | Denis Villeneuve |
| 10.4 东方武侠 | 库中无胡金铨；按题材取 Zhang Yimou 的群体几何或 Hou Hsiao-hsien 的远观层次，并说明 |
| 10.5 密色情绪 | Wong Kar-wai |
| 10.6 几何未知 | Stanley Kubrick |
| 10.7 时间废墟 | Andrei Tarkovsky |
| 10.8 远观东方 | Hou Hsiao-hsien 或 Akira Kurosawa |
| 10.9 冷灰未来 | Edward Yang（都市制度）或 David Fincher（监控式精密） |

与本 skill 其余规则的接口：

- 画幅 2.39:1。成品不是 2.39 时运行 `python3 -X utf8 scripts/crop_to_scope.py INPUT OUTPUT --anchor-x 0.5 --anchor-y 0.5`，用锚点保护偏心主体，不拉伸。脚本只依赖 ffmpeg，成功后打印 JSON 摘要；Windows 上没有 `python3` 时换成 `py -3`。
- 图像后端按第 2 节。引擎文件里的 “built-in image generation” 一律理解为用户指定的后端。
- 第 3 节五个判断同样适用：叙事瞬间必须是正在发生、尚未解决的动作，不是情绪摆拍。
- 第 6 节正向真实基底是地板，第四段在导演语法之上叠加它。导演语法明确要求的风格化（推颗粒、步进拖影、高饱和色块）优先于基底里的“克制”措辞，但皮肤质感、材质重量和可解释光源不让步。
- 第五段的 avoid-list 原样保留。它是单帧模式实测有效的部分，不套用第 6 节“只留四项结构性排除”；那条规则继续管三联与九镜。
- 第 9 节原创隔离适用。

成品是五段式：

1. native 2.39:1 frame + narrative instant + original setting
2. blocking + frame geometry + production-design details
3. camera position + one exact lens + focus + camera behavior
4. motivated light + palette + capture texture
5. emotional temperature + originality and avoid-list

交付用引擎文件 Output Format 的镜头卡（Mode / Strength / Director translation / Director DNA / Composition / Color signature / Recipe / Lens / Art direction / Ratio），加最终五段提示词和一句解读。用户只要图像时交付图像与镜头卡即可。

五段式用完整版。2026-10-01 在大香蕉、GPT、Seedream 上对照过：精简版没有一个模型赢，失分全在被压缩的走位和服装句上。必须缩短时只删第四段光色质感的重复描述，第二段原样保留。

后端是 Midjourney 时不出五段式，按第 7.5 节编译 MJ 短版。

### 7.2 三联

生成 3 张独立画面，再纵向拼接。禁止模型内拼图。

### 7.3 九镜

默认分三批生成：

- Batch A：Shot 1–3。
- Batch B：Shot 4–6。
- Batch C：Shot 7–9。

三镜一批可以降低长队列、整批失败和路径错配风险。每次返回后立即记录“shot number → prompt → file path”，再进入下一批。

只有工具明确保证独立结果、稳定顺序和部分失败可恢复时，才可并行九镜。不要仅凭文件修改时间推断镜头顺序。

### 7.4 部分失败恢复

若某一镜生成失败、被安全系统误拦截或严重漂移：

1. 盘点已成功落盘的镜头，不重复生成整组。
2. 保留失败镜的剧情功能、主要动作和连续性锚点。
3. 删除可能触发误判但并非剧情核心的措辞；用安全、非伤害、非剥削的视觉等价动作改写。
4. 只补跑失败镜。
5. 将补跑结果写回原镜号，再拼版。

不要因为一镜失败而改变整组角色、时代、色彩或结局。

### 7.5 后端为 Midjourney：编译短版

本节管所有模式。用户说要 MJ 版、Midjourney 提示词，或指定后端是 Midjourney 时，镜头卡、Continuity Bible 和镜头账本照常做，只把最终提示词换成 MJ 短版。原 midjourney-prompt skill 已于 2026-10-01 并入本节后退役。

五段式长散文不适合 Midjourney。同一场戏实测，MJ 吃长散文时主角偏位、琥珀色铺满屏幕、纹身串到其他角色、主角长成明星脸；改成短版后这几项基本消失。

交付形态：

- 每个镜头一段英文，约 150–190 词。
- 只交纯提示词，末尾不带任何 `--` 参数，连 `--ar` 也不带。比例、版本、风格化、分辨率由用户在 MJ 里自己设。
- 三联和九镜每镜一段，各自独立生成，再按第 8 节外部拼版。提示词里不写镜号，不写 triptych、grid、storyboard。

顺序：媒介与场景 → 主角身份锚点和动作（动作放进前两句）→ 其他角色各一句（`Left:` / `Right:` / `Foreground left edge:` 开头，每人一个动作）→ 背景 → 材质 → 光源（暖色点逐个列出）→ 色板 → 机位焦段 → 情绪。

实测得出的写法（2026-10-01，单帧科幻指挥舱两轮对照）：

- 每个角色的特征只写在他自己那一句里，醒目特征（纹身、伤疤、制服标识）只挂在一个人身上。MJ 会把相邻句子的特征串到别的角色上。
- 每个角色都要有位置词，前景遮挡人物要写全，例如 `Foreground left edge: the blurred back of a short-haired officer's head and shoulder`。省掉 "left edge" 和 "head" 时，MJ 会多生出一个遮挡人物，或者把他挪到画面中央。主角要居中就写 `dead center`。
- 暖色用枚举锁定：`the only warm light is X and Y`。
- 防明星脸用正写：年龄、发型、鼻子或伤痕、体型（如 thick heavy build，不写 muscular）。不靠否定词。
- 不带长否定列表；屏幕写成 `screens showing abstract graphs`，防止出现乱码文字。

从 midjourney-prompt 并入的通用写法：

- 人数要紧时，在开头写明确数量，例如 `exactly four people`，结尾再用一个短句重复一次。藏在长句中间的 single、one 管不住数量。
- 排除项写成画面里可见的正面状态，例如不要武器就写 `empty hands`。
- 一个镜头只保留一套视觉层级：光向、机位、时代、季节互相冲突时先在镜头卡里定下来，再写提示词。
- 只在用户明确要求时才写画面上的文字，并加引号、保持很短，同时提醒排版可能不准。
- 不写 masterpiece、best quality、8K、award-winning 这类空话。

多镜连续性（三联、九镜）：Continuity Bible 的角色锚点在每镜里用同一组英文措辞重复，词序也不变。MJ 没有上一张的记忆，措辞一变，人就可能变。这一条是按单帧实测外推的，三联和九镜还没有在 MJ 上实测过，出现漂移时先回来改这里。

实测备注（不是规则）：同一短版，加 `--raw --s 50` 的一组比默认设置更暗、更粗粝、更像实拍。

## 8. 拼版

九镜生成完成后运行：

```bash
python3 -X utf8 $HOME/Documents/Codex/cinema-dna-21x9x3/scripts/compose_nine_shot_storyboard.py --sources shot01.png shot02.png shot03.png shot04.png shot05.png shot06.png shot07.png shot08.png shot09.png --output-dir ./output/story-name --prefix story-name
```

实际源图路径按当前任务替换，不依赖某台电脑的固定盘符。这条命令在 macOS 终端、Windows PowerShell 和 Git Bash 里都能直接用；Windows 上没有 `python3` 时换成 `py -3`。脚本用 Python 调用 `ffmpeg` 完成缩放与拼版，无需额外 Python 包；`ffmpeg` 不在 PATH 时脚本会直接报错退出，不会静默产出残图。

可选参数：`--cell-width`（320–3840，默认 960）、`--cell-height`（134–1607，默认 402）、`--gap`（0–64，默认 8）。默认值下总览为 2896×1222，每张三联为 1920×2425。

成功后脚本向 stdout 打印 JSON 摘要（`ShotCount`、`TriptychCount`、`ContactSheet`、画布尺寸），据此核对产物齐全，不要凭假设汇报。

脚本必须：

- 验证正好 9 个可读源文件。
- 保留九张按编号命名的独立源图。
- 保持纵横比，不拉伸画面。
- 输出三张纵向三联图。
- 输出一张 3×3 九宫格。
- 使用黑色 8–12 px 呼吸间隔。
- 不添加文字、序号、水印和装饰边框。

## 9. 参考图与原创隔离

参考图只允许抽取一个主维度：

1. 构图方法。
2. 配色方法。
3. 题材方向。

其余维度必须原创。禁止复用相同人物数量与位置、人物关系、动作节点、道具组合、空间骨架、标志性机位、综合色与剧情结果。

若同时借用两个以上主要维度，或一眼能认出某个具体电影静帧、海报或现成 IP 的轮廓，必须重写。最终提示词不要依赖导演名或电影名，把审美翻译成可见的布景、服装、光源、构图、材质和曝光事实。

## 10. 质量验收

生成前和交付前都检查。

### 10.1 故事

- 不可解决状态是否能用一句事实说明？
- 每镜是否只有一个主要动作？
- 镜头顺序能否随意打乱？若可以，剪辑关系不成立。
- 是否出现选择、代价、后果或未完成余韵？
- 是否靠万能纸条、钥匙、照片或夸张表情解释剧情？

### 10.2 连续性

- 主角年龄段、发型、服装主色和识别物是否稳定？
- 关键道具颜色、形状和使用状态是否连续？
- 运动方向、空间轴线和天气是否出现无动机跳变？
- 补跑镜头是否回到原镜号和原叙事功能？

### 10.3 导演感

- 摄影机为什么在这里？
- 观众处于什么观看立场？
- 每镜的视线入口、落点和出口是否不同？
- 九镜是否避免连续重复门框、背影、中心走廊、眼部特写和低机位？
- 是否允许一张普通但必要的过渡镜头？

### 10.4 真实电影

- 是否像真人、实景和真实摄影机？
- 光、烟、反射和色彩是否有物理来源？
- 皮肤、衣物、金属、木材和混凝土是否有重量？
- 是否所有细节都过度清晰、昂贵或漂亮？
- 是否像广告、游戏、CG、短剧或电视剧？

### 10.5 文件

- 独立镜头数量是否符合本次模式和用户要求（默认 Single 1 张、Triptych 3 张、Nine-Shot 9 张）？
- 每张是否可读取且接近 2.39:1？
- 需要拼版时，是否由已生成的独立镜头外部拼接；Single 不要求拼版？
- Nine-Shot 是否按 1→9 从左到右、从上到下排列；Triptych 是否按约定顺序拼接？
- 是否保留了可单独补跑的源图？

下表用于需要比较方案时的内部参考，不设主观分数交付门槛。检查范围随 Single、Triptych、Nine-Shot 或只交文字的任务变化；只修正影响身份、连续性、可读性或所需文件完整性的具体缺陷，通过后不重复评分或重做：

| 项目 | 分值 |
|---|---:|
| 剧情因果与不可打乱性 | 25 |
| 连续性圣经执行 | 20 |
| 构图、视线与观看立场 | 20 |
| 色彩和光源物理可信 | 15 |
| 真人实景与反 AI 质感 | 15 |
| 文件与拼版完整性 | 5 |

以下是对应模式中的实质缺陷；只交文字时不要求已生成文件，不把不适用项作为阻断：

- 用户要求独立源图与外部拼版，却仅交付模型一次生成的九宫格。
- 图像交付任务缺少用户要求的独立源图。
- 九镜只是同一构图、同一动作换角度。
- 明显 CG、游戏宣传图或商业广告。
- 人物、关键道具或空间在关键因果镜头中无理由变形。

## 11. 默认交付

    ## 片名或主题
    - Logline：
    - 模式：Single / Triptych / Nine-Shot
    - 色彩命题：
    - 成像基底：

    ### 独立镜头
    - Shot 01：
    - ...

    ### 拼版
    - 三联或九宫格：

    ### 核验
    - 独立源图数量：
    - 画幅：
    - 拼版顺序：
    - 补跑记录：

用户只要图像时，交付图像和必要文件链接即可，不重复输出所有提示词。

Single 模式改用第 7.1 节的镜头卡格式，不套用上面的多镜模板。

## 12. 按需读取

当前用户要求与本文件的模式、工具和连续性规则优先。full-spec 可取的章节：第 5 节常用三联叙事模板、第 6.1.4 节光学缺陷系统、第 9 节八个电影视觉主引擎、第 10 节（含 10.10–10.11）导演与电影 DNA 库、第 12 节镜头选择规则、第 13–17 节构图与场面调度 / 光线 / 色彩 / 人物处理 / 建筑、空间、产品转换规则；镜头职责按本文件第 5 节的镜头账本设计。

- 单帧任务：必须读取 [references/director-frame/single-frame-engine.md](references/director-frame/single-frame-engine.md)，并按第 7.1 节路由读取 `references/director-frame/` 下的导演语法、构图几何、色彩配方、焦段与材质文件。这组文件是英文，按 24 位具名导演组织；full-spec 第 10 节的 DNA 族是它们的中文抽象版，按第 7.1 节映射表对应，不要并行引用两套说法。后端为 Midjourney 时，所有模式都按第 7.5 节编译短版，只交纯提示词。
- 九镜故事任务：必须读取 [references/nine-shot-story-protocol-v3.md](references/nine-shot-story-protocol-v3.md)。
- 输出仍显得油腻、过度精致、过脏或镜头节奏常规时：读取 [references/cinema-dna-v4-anti-ai.md](references/cinema-dna-v4-anti-ai.md)。
- 需要更完整的单帧、三联、焦段、光学和题材方法库时：按上面列出的章节标题定位读取 [references/cinema-dna-full-spec.md](references/cinema-dna-full-spec.md)，不整份加载。

## 13. 最终原则

**构图不是装饰，而是人物与空间之间的权力关系。**

**色彩不是滤镜，而是事件发生方式的一部分。**

**连续性不是重复长提示词，而是少量稳定锚点在每个镜头中被准确继承。**

**九宫格不是一张复杂图片，而是九个可单独替换、按因果剪辑的独立镜头。**

**电影感不是颗粒、色散和黑边，而是摄影机在正确的位置拍到了正确的停顿。**

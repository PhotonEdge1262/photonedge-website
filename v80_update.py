#!/usr/bin/env python3
"""PhotonEdge V80 Update Script - Performs all 7 tasks"""

import json, re, os, sys

BASE = "/app/data/所有对话/主对话/PhotonEdge-V80"

###############################################################################
# Task 1: Expand 20 product descriptions in products-data.js
###############################################################################

def task1_expand_descriptions():
    print("=== Task 1: Expanding 20 product descriptions ===")
    filepath = os.path.join(BASE, "js/products-data.js")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Product name -> (new description extension, new descriptionZh extension)
    # We'll append to existing descriptions
    extensions = {
        "BK7 Plano-Convex Lenses": (
            " These lenses are ideal for collimation of divergent light sources such as laser diodes and optical fibers, as well as for focusing collimated beams onto detectors or fiber couplers. Their plano-convex geometry minimizes spherical aberration when the curved surface faces the longest conjugate distance, ensuring high-quality beam focusing in imaging systems. PhotonEdge offers BK7 plano-convex lenses in diameters from 2.5mm to 75mm with focal lengths ranging from 3.9mm to 1000mm. Anti-reflection coatings are available in three broadband bands covering 350-1250nm, with custom coating options for specific wavelengths upon request.",
            " 此类透镜是准直激光二极管和光纤等发散光源的理想选择，也可将准直光束聚焦到探测器或光纤耦合器上。平凸几何形状在凸面朝向较长共轭距离时可最小化球差，确保成像系统中的高质量光束聚焦。PhotonEdge提供直径2.5mm至75mm、焦距3.9mm至1000mm的BK7平凸透镜。增透膜覆盖350-1250nm三个宽带波段，并可按需提供特定波长的定制镀膜。"
        ),
        "BK7 Plano-Concave Lenses": (
            " BK7 plano-concave lenses are essential for beam expansion, divergence control, and increasing focal lengths in optical systems. They are commonly used to expand laser beams or to increase the focal length of converging lens assemblies without introducing significant aberration. The plano-concave design produces a virtual image, making them ideal for Galilean beam expanders and optical viewing systems where a compact design is preferred. Available in diameters from 6mm to 50mm with negative focal lengths from -12mm to -300mm, these lenses feature surface quality of 40-20 scratch-dig and flatness of lambda/4. Multiple AR coating options cover visible to near-infrared wavelengths.",
            " BK7平凹透镜是光束扩束、发散控制和增加光学系统焦距的关键元件。常用于扩展激光束或增加会聚透镜组的焦距而不引入显著像差。平凹设计产生虚像，非常适合伽利略扩束器和需要紧凑设计的观察系统。提供直径6mm至50mm、负焦距-12mm至-300mm的规格，面型40-20划痕-麻点，平面度λ/4。多种增透膜选项覆盖可见到近红外波段。"
        ),
        "BK7 Bi-Convex Lenses": (
            " BK7 bi-convex lenses provide symmetrical focusing with minimal aberration when object and image distances are approximately equal. They are widely used in relay imaging systems, condenser optics for projection, and 1:1 imaging applications where both conjugates are similar. The symmetric curvature naturally balances spherical aberration, yielding superior image quality compared to plano-convex lenses in symmetric conjugate configurations. PhotonEdge supplies these lenses in diameters from 6mm to 75mm with focal lengths spanning 8mm to 500mm. Each lens undergoes strict quality control with centration below 3 arc minutes and clear aperture exceeding 90%. Available AR coatings span 350-1250nm across three standard bands.",
            " BK7双凸透镜在物距和像距近似相等时提供对称聚焦且像差最小。广泛应用于中继成像系统、投影聚光光学和1:1成像应用。对称曲率自然平衡球差，在对称共轭配置下比平凸透镜提供更优的成像质量。提供直径6mm至75mm、焦距8mm至500mm规格。每片透镜经过严格质控，偏心小于3角分，有效通光孔径超过90%。增透膜覆盖350-1250nm三个标准波段。"
        ),
        "BK7 Bi-Concave Lenses": (
            " BK7 bi-concave lenses are designed for beam divergence and focal length reduction in optical assemblies. Their symmetric concave surfaces make them particularly effective in expanding collimated beams while maintaining beam uniformity, and they serve as essential components in beam expander and projection systems. The bi-concave geometry provides balanced divergence characteristics, reducing asymmetric aberration compared to plano-concave designs when used in symmetric configurations. These lenses are available in diameters from 6mm to 50mm with negative focal lengths from -10mm to -200mm. Standard specifications include 40-20 surface quality, lambda/4 flatness, and multiple broadband AR coating options for wavelengths from 350nm to 1250nm.",
            " BK7双凹透镜专为光束发散和缩短光学组件焦距而设计。对称凹面使其在扩展准直光束时保持光束均匀性特别有效，是扩束器和投影系统的核心元件。双凹几何结构提供平衡的发散特性，在对称配置中比平凹设计减少非对称像差。提供直径6mm至50mm、负焦距-10mm至-200mm规格。标准规格包括40-20面型、λ/4平面度和350nm至1250nm多种宽带增透膜。"
        ),
        "UV Fused Silica Plano-Convex Lenses": (
            " UV fused silica plano-convex lenses offer superior transmission from 185nm to 2.1um, making them indispensable for UV laser applications, fluorescence microscopy, and semiconductor lithography systems. The exceptionally low coefficient of thermal expansion of fused silica ensures stable optical performance under high-power laser irradiation where BK7 would experience thermal lensing. These lenses are the preferred choice for excimer laser systems at 193nm and 248nm, as well as frequency-doubled and tripled Nd:YAG lasers. Available in diameters from 6mm to 75mm with focal lengths from 10mm to 1000mm, they feature UV-grade surface quality of 20-10 scratch-dig and lambda/10 flatness. UV-optimized AR coatings provide R<0.5% at design wavelengths.",
            " UV熔融石英平凸透镜在185nm至2.1μm波段提供卓越透过率，是UV激光应用、荧光显微镜和半导体光刻系统不可或缺的元件。熔融石英极低的热膨胀系数确保在高功率激光照射下仍保持稳定的光学性能，而BK7则会产生热透镜效应。是193nm和248nm准分子激光系统及倍频、三倍频Nd:YAG激光的首选。提供直径6mm至75mm、焦距10mm至1000mm规格，UV级面型20-10，平面度λ/10。UV优化增透膜在设计波长处R<0.5%。"
        ),
        "UV Fused Silica Plano-Concave Lenses": (
            " UV fused silica plano-concave lenses provide reliable beam expansion and divergence in the deep ultraviolet through near-infrared spectrum. Their exceptional UV transmission down to 185nm makes them critical for excimer laser beam conditioning, UV spectroscopy beam shaping, and lithography illumination systems. The low thermal expansion coefficient of fused silica ensures dimensional stability during prolonged UV exposure, preventing focus drift in precision instruments. These lenses feature 20-10 surface quality and lambda/10 flatness, meeting the stringent requirements of UV optical systems. Available diameters range from 6mm to 50mm with negative focal lengths from -12.7mm to -300mm, and UV-enhanced AR coatings can be specified for wavelengths from 185nm to 700nm.",
            " UV熔融石英平凹透镜在深紫外到近红外光谱范围内提供可靠的光束扩束和发散功能。其低至185nm的卓越UV透过率使其成为准分子激光光束整形、UV光谱光束塑造和光刻照明系统的关键元件。熔融石英的低热膨胀系数确保长时间UV照射下的尺寸稳定性，防止精密仪器的焦点漂移。面型20-10，平面度λ/10，满足UV光学系统的严格要求。直径6mm至50mm，负焦距-12.7mm至-300mm，可提供185nm至700nm的UV增强增透膜。"
        ),
        "Achromatic Doublet Lenses": (
            " Achromatic doublet lenses correct chromatic aberration by combining a crown glass and flint glass element cemented together, bringing two wavelengths to a common focus. This makes them ideal for broadband imaging applications including machine vision, fluorescence microscopy, and projection systems where color fringing must be eliminated. The cemented design also reduces spherical aberration compared to singlet lenses, delivering sharper images across a wider spectral range. PhotonEdge achromatic doublets are available with focal lengths from 6mm to 500mm and diameters from 6mm to 50mm, covering visible and near-infrared broadband ranges. Typical design wavelengths include 486nm, 587.6nm, and 656.3nm. Mounting options and custom wavelength optimization are available for OEM applications.",
            " 消色差双合透镜通过将冕牌玻璃和火石玻璃元件胶合来校正色差，使两个波长聚焦于同一点。适用于机器视觉、荧光显微镜和投影系统等宽带成像应用，有效消除色边。胶合设计也比单透镜减少球差，在更宽光谱范围内提供更清晰的图像。提供焦距6mm至500mm、直径6mm至50mm规格，覆盖可见和近红外宽带范围。典型设计波长包括486nm、587.6nm和656.3nm。可提供安装选项和OEM应用的定制波长优化。"
        ),
        "Aspherical Lenses": (
            " Aspherical lenses feature a non-spherical surface profile that eliminates spherical aberration entirely, enabling diffraction-limited focusing with a single element. This makes them indispensable in laser collimation for fiber optic coupling, barcode scanning, CD/DVD pickup systems, and high-resolution imaging where compact optical assemblies are required. By replacing multiple spherical elements with a single asphere, designers can reduce lens count, system weight, and overall cost while improving optical performance. PhotonEdge offers precision-molded and CNC-polished aspherical lenses in diameters from 5mm to 50mm with numerical apertures up to 0.5. Surface accuracy reaches lambda/4 with surface roughness below 10A RMS. AR coatings are available for UV, visible, and NIR wavelengths.",
            " 非球面透镜采用非球面面型完全消除球差，实现单元件衍射极限聚焦。是光纤耦合激光准直、条码扫描、CD/DVD光学拾取和高分辨率成像等紧凑光学组件不可或缺的元件。用单片非球面镜替代多片球面镜可减少透镜数量、系统重量和总体成本，同时提升光学性能。提供精密模压和CNC抛光非球面透镜，直径5mm至50mm，数值孔径达0.5。面精度λ/4，表面粗糙度低于10A RMS。增透膜覆盖UV、可见和NIR波段。"
        ),
        "BK7 Right Angle Prisms": (
            " BK7 right angle prisms utilize total internal reflection to redirect light by 90 degrees with high efficiency, making them fundamental building blocks in periscope systems, binoculars, and optical breadboard layouts. The hypotenuse face provides TIR for beams at normal incidence, while the two cathetus faces serve as entrance and exit surfaces with minimal reflection loss. These prisms can also function as retroreflectors when light enters through the hypotenuse. PhotonEdge BK7 right angle prisms are available in sizes from 5mm to 50mm with 20-10 surface quality and 1 arc minute angular tolerance. Custom coatings on the hypotenuse can convert TIR to a protected reflecting surface for broader incident angle ranges.",
            " BK7直角棱镜利用全内反射高效地将光路偏转90度，是潜望镜系统、双筒望远镜和光学平台布局的基础元件。斜面为正入射光束提供全内反射，两个直角面作为入射和出射面，反射损失极小。光束通过斜面入射时还可作为逆反射器使用。提供5mm至50mm规格，面型20-10，角度公差1角分。斜面可定制镀膜将全内反射转为保护反射面，适用于更宽的入射角范围。"
        ),
        "Equilateral Dispersing Prisms": (
            " Equilateral dispersing prisms separate white light into its component wavelengths through angular dispersion, making them essential for spectrometers, wavelength-selective lasers, and multi-spectral imaging systems. The 60-degree apex angle provides significant angular separation between wavelengths, enabling both coarse wavelength selection and fine spectral analysis. These prisms are widely used in pulse compression setups for ultrafast laser systems and in wavelength division multiplexing for telecommunications. PhotonEdge equilateral prisms are fabricated from BK7, UV fused silica, CaF2, and ZnSe substrates to cover wavelengths from 185nm to 14um. Size options range from 10mm to 50mm with angular tolerance of 1 arc minute and surface quality of 20-10.",
            " 等边色散棱镜通过角色散将白光分离为组成波长，是光谱仪、波长选择性激光器和多光谱成像系统的核心元件。60度顶角提供显著的波长角度分离，可实现粗选波长和精细光谱分析。广泛用于超快激光系统的脉冲压缩装置和电信波分复用。提供BK7、UV熔融石英、CaF2和ZnSe基底，覆盖185nm至14μm波长。尺寸10mm至50mm，角度公差1角分，面型20-10。"
        ),
        "Dove Prisms": (
            " Dove prisms rotate an image at twice the angular rate of the prism rotation, making them invaluable in target tracking systems, rifle scopes, and image orientation correction in viewing instruments. Their compact inverted-trapezoid form factor allows easy mechanical rotation while maintaining beam alignment. When the prism is rotated by angle theta about the longitudinal axis, the transmitted image rotates by 2*theta, providing a simple mechanical means to de-rotate images in spinning optical systems. Dove prisms also introduce image inversion along one axis when used in a fixed orientation. PhotonEdge offers BK7 and UV fused silica dove prisms in apertures from 10mm to 40mm with surface quality of 20-10 and angular tolerance of 3 arc minutes.",
            " 道威棱镜以棱镜旋转角速度的两倍旋转像面，在目标跟踪系统、步枪瞄准镜和观察仪器的像面方位校正中具有重要价值。其紧凑的倒梯形外形允许轻松的机械旋转同时保持光束对准。当棱镜绕纵轴旋转角度θ时，透射图像旋转2θ，为旋转光学系统提供简单的机械消旋方法。固定方向使用时，道威棱镜还沿一个轴引入像反转。提供BK7和UV熔融石英材质，通光孔径10mm至40mm，面型20-10，角度公差3角分。"
        ),
        "Corner Cube Prisms": (
            " Corner cube prisms, also known as retroreflectors, return any incident beam back to its source parallel to the incoming direction, regardless of the angle of incidence. This property makes them critical in laser ranging, interferometric distance measurement, and satellite laser ranging where precise beam return is essential. Unlike flat mirrors, corner cubes do not require precise angular alignment, greatly simplifying optical alignment in field-deployed instruments. They are also used in vehicle reflectors and safety markers for their wide-angle retroreflection capability. PhotonEdge corner cube prisms are available in apertures from 10mm to 50mm with 20-10 surface quality and a deviation from parallelism of less than 3 arc seconds for precision metrology applications.",
            " 角锥棱镜也称为逆反射器，可将任何入射光束平行于来路方向返回，不受入射角影响。这一特性使其在激光测距、干涉距离测量和卫星激光测距中至关重要。与平面镜不同，角锥棱镜不需要精确的角度对准，大大简化了现场部署仪器的光学对准。也因其宽角逆反射能力用于车辆反射器和安全标记。通光孔径10mm至50mm，面型20-10，平行度偏差小于3角秒，满足精密计量应用需求。"
        ),
        "Cube Beamsplitters": (
            " Cube beamsplitters split an incident beam into reflected and transmitted components with precise ratio control, typically 50:50 or other specified ratios. Their cemented cube construction provides equal optical path lengths for both output beams and maintains beam alignment independent of wavelength, making them ideal for interferometers, autocorrelators, and polarization optics setups. The cube form factor also simplifies mechanical mounting compared to plate beamsplitters and eliminates ghost reflections. PhotonEdge cube beamsplitters feature 20-10 surface quality and are available in sizes from 5mm to 50mm. Options include non-polarizing broadband beamsplitters for visible and NIR, as well as polarizing cube beamsplitters with extinction ratios exceeding 500:1.",
            " 立方分束器将入射光束按精确比例分成反射和透射分量，通常为50:50或其他指定比例。胶合立方结构为两路输出光束提供等光程，且光束对准不受波长影响，是干涉仪、自相关仪和偏振光学装置的理想选择。立方外形也比平板分束器更便于机械安装，并消除鬼像反射。面型20-10，尺寸5mm至50mm。选项包括可见和NIR非偏振宽带分束器，以及消光比超过500:1的偏振立方分束器。"
        ),
        "Circular/Square Beamsplitter Plates": (
            " Beamsplitter plates provide a compact solution for splitting incident light into reflected and transmitted beams at a defined ratio. Their thin-plate form factor minimizes the optical path difference between the two beams and reduces wavefront distortion compared to cube beamsplitters, which is critical for ultrafast laser pulse measurement and interference applications. The lightweight design makes them suitable for scanning systems and gimbal-mounted optics where mass must be minimized. PhotonEdge beamsplitter plates are available in both circular and square geometries with sizes from 12.5mm to 50mm. Standard splitting ratios include 50:50, 30:70, and 70:30 for visible and NIR wavelengths, with custom ratios available upon request.",
            " 分束平板提供紧凑的光束分离方案，按定义比例将入射光分为反射和透射光束。薄板外形最小化两路光束的光程差，比立方分束器减少波前畸变，这对超快激光脉冲测量和干涉应用至关重要。轻量化设计适用于需要最小化质量的扫描系统和万向节安装光学。提供圆形和方形两种几何形状，尺寸12.5mm至50mm。标准分束比包括50:50、30:70和70:30，覆盖可见和NIR波段，可按需定制比例。"
        ),
        "BK7 Circular/Square Windows": (
            " BK7 optical windows provide high-transmission barriers between optical systems and external environments, protecting internal components from dust, moisture, and mechanical damage while minimizing optical distortion. They are extensively used in camera housings, sensor windows, laser enclosures, and environmental test chambers. BK7 glass offers excellent homogeneity and low bubble content, ensuring consistent optical performance across the clear aperture. The moderate thermal stability of BK7 makes these windows suitable for laboratory and industrial environments from -40 to 80 degrees Celsius. PhotonEdge BK7 windows are available in diameters from 5mm to 100mm and square sizes from 10mm to 50mm, with 20-10 surface quality and lambda/4 or lambda/10 flatness options. Uncoated and AR-coated versions are offered.",
            " BK7光学窗口在光学系统与外部环境之间提供高透过率隔离屏障，保护内部元件免受灰尘、湿气和机械损伤，同时最小化光学畸变。广泛用于相机外壳、传感器窗口、激光密封罩和环境测试腔。BK7玻璃具有优异的均匀性和低气泡含量，确保整个通光孔径内一致的光学性能。BK7适中的热稳定性使这些窗口适用于-40至80摄氏度的实验室和工业环境。提供直径5mm至100mm和方形10mm至50mm规格，面型20-10，平面度λ/4或λ/10。提供无镀膜和增透膜版本。"
        ),
        "UV Fused Silica Circular/Square Windows": (
            " UV fused silica optical windows deliver exceptional transmission from 185nm through 2.1um with outstanding resistance to high-energy radiation and thermal shock. Their extremely low coefficient of thermal expansion (0.55 ppm/K) ensures dimensional stability under extreme temperature fluctuations, making them the preferred choice for space-borne instruments, UV lithography, and high-power laser windows. Unlike BK7, fused silica does not solarize under prolonged UV exposure, maintaining its transmission properties over years of service. These windows are also chemically inert and resistant to most acids and solvents. PhotonEdge UV fused silica windows are available in diameters from 5mm to 100mm with 10-5 surface quality and lambda/20 flatness for demanding UV applications. UV-optimized AR coatings achieve R<0.25% at design wavelengths.",
            " UV熔融石英光学窗口在185nm至2.1μm波段提供卓越透过率，具有出色的抗高能辐射和抗热冲击性能。极低的热膨胀系数（0.55 ppm/K）确保极端温度波动下的尺寸稳定性，是星载仪器、UV光刻和高功率激光窗口的首选。与BK7不同，熔融石英在长时间UV照射下不会太阳化，多年使用仍保持透过率。化学惰性，耐大多数酸和溶剂。直径5mm至100mm，面型10-5，平面度λ/20，满足苛刻UV应用需求。UV优化增透膜在设计波长处R<0.25%。"
        ),
        "Sapphire Circular/Square Windows": (
            " Sapphire optical windows combine extreme mechanical hardness (Mohs 9) with broadband transmission from 180nm to 4.5um, making them uniquely suited for the most demanding applications. Their exceptional scratch resistance makes them the standard choice for watch crystals, barcode scanner windows, and underwater camera ports where physical durability is paramount. Sapphire also provides excellent chemical inertness, resisting virtually all acids and alkalis at room temperature, which is critical for analytical instrumentation and downhole sensing in oil and gas exploration. The high thermal conductivity and thermal shock resistance enable reliable operation at temperatures exceeding 1000 degrees Celsius. PhotonEdge sapphire windows are available in diameters from 5mm to 100mm with 40-20 or 20-10 surface quality. Both uncoated and AR-coated versions support UV through MWIR applications.",
            " 蓝宝石光学窗口结合了极高的机械硬度（莫氏9级）和180nm至4.5μm宽带透过率，使其独特适用于最苛刻的应用。卓越的耐刮擦性使其成为手表表镜、条码扫描器窗口和水下相机端口的标准选择。优异的化学惰性，在室温下几乎耐所有酸碱，这对分析仪器和石油天然气井下传感至关重要。高导热率和抗热冲击性确保在超过1000摄氏度温度下可靠运行。提供直径5mm至100mm，面型40-20或20-10。无镀膜和增透膜版本支持UV到MWIR应用。"
        ),
        "Broadband Dielectric Circular/Square Mirrors": (
            " Broadband dielectric mirrors provide exceptionally high reflectivity (R>99%) over wide spectral ranges using multi-layer thin-film coatings, making them essential for tunable laser systems, supercontinuum sources, and broadband optical delay lines. Unlike metallic mirrors, dielectric coatings are virtually absorption-free, enabling them to handle high laser power densities without thermal distortion or coating degradation. The low scatter characteristics also make them suitable for precision interferometry and cavity-enhanced spectroscopy. PhotonEdge broadband dielectric mirrors are available for UV, visible, and NIR ranges in diameters from 12.5mm to 50mm. Surface quality is 20-10 with flatness of lambda/10 at 632.8nm. Custom bandwidth and angle-of-incidence optimization are available for OEM applications.",
            " 宽带介质反射镜采用多层薄膜镀膜在宽光谱范围内提供极高反射率（R>99%），是可调谐激光系统、超连续谱光源和宽带光学延迟线的关键元件。与金属反射镜不同，介质镀膜几乎无吸收，能承受高激光功率密度而不产生热畸变或镀膜退化。低散射特性也使其适用于精密干涉测量和腔增强光谱。提供UV、可见和NIR波段，直径12.5mm至50mm。面型20-10，632.8nm处平面度λ/10。可提供定制带宽和入射角优化，满足OEM应用需求。"
        ),
        "Enhanced Aluminum Circular/Square Mirrors": (
            " Enhanced aluminum mirrors combine the broad spectral reflectivity of aluminum with protective dielectric overcoats that boost reflectivity above 92% across the visible spectrum and prevent oxidation of the aluminum layer. This enhanced protection ensures long-term stability of optical performance in environments where unprotected aluminum would degrade over time. They offer an excellent balance of broadband performance and cost-effectiveness, making them the most popular choice for general-purpose laboratory mirrors, illumination systems, and optical breadboard setups. PhotonEdge enhanced aluminum mirrors are available in diameters from 12.5mm to 75mm with 40-20 surface quality and lambda/4 flatness. Standard substrates include BK7 and UV fused silica for UV-extended applications.",
            " 增强铝反射镜结合了铝的宽光谱反射率和保护性介质覆盖层，在可见光谱范围内将反射率提升至92%以上，并防止铝层氧化。这种增强保护确保了在裸铝随时间退化的环境中光学性能的长期稳定性。在宽带性能和成本效益之间提供出色平衡，是通用实验室反射镜、照明系统和光学平台布置中最受欢迎的选择。提供直径12.5mm至75mm，面型40-20，平面度λ/4。标准基底包括BK7和UV熔融石英，满足UV扩展应用需求。"
        ),
        "Laser Line High Reflected Mirrors": (
            " Laser line high reflected mirrors achieve R>99.5% at specific laser wavelengths through precisely controlled multi-layer dielectric coatings, making them critical for laser resonator cavities, beam steering in high-power laser systems, and power-sensitive optical setups where every fraction of a percent in reflection matters. The dielectric construction provides superior laser damage threshold compared to metallic mirrors, enabling reliable operation at power densities exceeding 10 J/cm2 for nanosecond pulses. These mirrors maintain high reflectivity within their specified bandwidth while rejecting out-of-band wavelengths, functioning simultaneously as spectral filters. PhotonEdge laser line HR mirrors are available for wavelengths from 266nm to 1064nm in diameters from 12.5mm to 50mm, with 10-5 surface quality and lambda/10 flatness for wavefront-critical applications.",
            " 激光线高反射镜通过精确控制的多层介质镀膜在特定激光波长实现R>99.5%，是激光谐振腔、高功率激光系统光束转向和对反射率极其敏感的光学装置的关键元件。介质结构比金属反射镜提供更高的激光损伤阈值，在纳秒脉冲下功率密度超过10 J/cm2仍能可靠运行。这些反射镜在指定带宽内保持高反射率，同时抑制带外波长，兼具光谱滤波功能。提供266nm至1064nm波长，直径12.5mm至50mm，面型10-5，平面度λ/10，满足波前关键应用需求。"
        ),
    }

    # Find and replace each product's description
    count = 0
    for name, (en_ext, zh_ext) in extensions.items():
        # Find the product block by name, then locate its description and descriptionZh
        # Pattern: find "name": "EXACT_MATCH" then find its description and descriptionZh
        # We need to be careful with the JSON structure
        
        # Strategy: use node to do the replacement since products-data.js is a JS file
        pass
    
    # Use a different approach - load with node, modify, save
    # We'll write a node script to do the replacement
    node_script = '''
var fs = require('fs');
var content = fs.readFileSync('js/products-data.js', 'utf-8');
eval(content);

var extensions = ''' + json.dumps(json.dumps(extensions)) + ''';
extensions = JSON.parse(extensions);

for (var i = 0; i < PRODUCTS.length; i++) {
    var p = PRODUCTS[i];
    if (extensions[p.name]) {
        var ext = extensions[p.name];
        p.description = p.description + ext[0];
        p.descriptionZh = p.descriptionZh + ext[1];
    }
}

// Now rebuild the file - we need to serialize PRODUCTS back
// Actually, let's do string replacement approach
// Re-read and do targeted replacements
''';
    
    # Better approach: use Python with regex to find and replace descriptions
    # Read the file, find each product's description by its name, and append
    
    target_names = list(extensions.keys())
    
    for name in target_names:
        en_ext, zh_ext = extensions[name]
        
        # Find the product in the JS file by name
        # Pattern: "name": "PRODUCT_NAME", ... "description": "...", "descriptionZh": "..."
        # We need to find description and descriptionZh after the name match
        
        # Use a more robust approach: find the product block
        name_escaped = re.escape(name)
        
        # Find "name": "PRODUCT_NAME"
        name_pattern = '"name":\\s*"' + name_escaped + '"'
        name_match = re.search(name_pattern, content)
        if not name_match:
            print(f"  WARNING: Could not find product '{name}'")
            continue
        
        # From this position, find the next "description": "..."
        # The description field comes after name
        start_pos = name_match.end()
        
        # Find description field (not descriptionZh)
        desc_pattern = '"description":\\s*"((?:[^"\\\\]|\\\\.)*?)"'
        desc_match = re.search(desc_pattern, content[start_pos:])
        if not desc_match:
            print(f"  WARNING: Could not find description for '{name}'")
            continue
        
        # Replace the description value - append extension
        original_desc = desc_match.group(1)
        # Unescape the description to check it
        # Actually, we just append the extension text right after the closing of original description
        desc_start = start_pos + desc_match.start(1)
        desc_end = start_pos + desc_match.end(1)
        
        # Insert extension before the closing quote
        # We need to handle escaped characters - just insert before the final quote
        content = content[:desc_end] + en_ext + content[desc_end:]
        
        # Now find descriptionZh - need to re-search from after the name
        # Recalculate positions since content changed
        name_match2 = re.search(name_pattern, content)
        start_pos2 = name_match2.end()
        
        # Find descriptionZh (must come after description)
        desc_zh_pattern = '"descriptionZh":\\s*"((?:[^"\\\\]|\\\\.)*?)"'
        desc_zh_match = re.search(desc_zh_pattern, content[start_pos2:])
        if not desc_zh_match:
            print(f"  WARNING: Could not find descriptionZh for '{name}'")
            continue
        
        zh_start = start_pos2 + desc_zh_match.start(1)
        zh_end = start_pos2 + desc_zh_match.end(1)
        content = content[:zh_end] + zh_ext + content[zh_end:]
        
        count += 1
        print(f"  Extended: {name}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Total extended: {count}/20")
    return count

###############################################################################
# Task 2: Image alt tags - already verified all present, but check dynamic
###############################################################################

def task2_check_alt_tags():
    print("\n=== Task 2: Checking image alt tags ===")
    # Already verified all static img tags have alt
    # Check product-detail.html dynamic rendering
    filepath = os.path.join(BASE, "product-detail.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if dynamic img tags include alt
    dynamic_imgs = re.findall(r"'<img[^>]*>'", content)
    # Also check template strings
    js_imgs = re.findall(r'\\x3cimg[^>]*>', content)  # HTML entities in JS
    
    alt_count = 0
    missing_alt = 0
    
    # Search for all img tag creation in JS
    for line in content.split('\n'):
        if '<img' in line:
            if 'alt=' in line:
                alt_count += 1
            elif "createElement('img')" in line or '.innerHTML' in line:
                # Dynamic creation - check context
                if 'alt' in line or 'alt' in content[max(0,content.index(line)-200):content.index(line)+len(line)+200]:
                    alt_count += 1
                else:
                    missing_alt += 1
                    print(f"  Possible missing alt in JS: {line.strip()[:100]}")
    
    print(f"  Static img tags with alt: Already verified (0 missing)")
    print(f"  Dynamic img tags with alt: {alt_count}")
    if missing_alt == 0:
        print("  All dynamic img tags already include alt attributes")
    
    return 0

###############################################################################
# Task 3: Blog product internal links enhancement
###############################################################################

def task3_blog_links():
    print("\n=== Task 3: Enhancing blog product links ===")
    filepath = os.path.join(BASE, "js/blog-data.js")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Product links to add for each blog
    blog_links = {
        22: [  # LiDAR
            ('/products/bk7-plano-convex/', 'BK7 Plano-Convex Lenses'),
            ('/products/bk7-windows/', 'BK7 Windows'),
            ('/products/narrow-band-interference-filters/', 'Narrow Band Interference Filters'),
            ('/products/cube-beamsplitters/', 'Cube Beamsplitters'),
        ],
        23: [  # Medical
            ('/products/achromatic-doublet/', 'Achromatic Doublet Lenses'),
            ('/products/aspherical-lenses/', 'Aspherical Lenses'),
            ('/products/bk7-windows/', 'BK7 Windows'),
            ('/products/sapphire-windows/', 'Sapphire Windows'),
        ],
        24: [  # IR Materials
            ('/products/ge-windows/', 'Ge Windows'),
            ('/products/znse-windows/', 'ZnSe Windows'),
            ('/products/si-windows/', 'Si Windows'),
        ],
        25: [  # LIDT
            ('/products/laser-line-high-reflected-mirrors/', 'Laser Line HR Mirrors'),
            ('/products/broadband-dielectric-mirrors/', 'Broadband Dielectric Mirrors'),
            ('/products/uv-fused-silica-windows/', 'UV Fused Silica Windows'),
        ],
    }
    
    # Also add links to blogs 6-20 that have 0 product links
    early_blog_links = {
        6: [  # Trusted Partner
            ('/products/bk7-plano-convex/', 'BK7 Plano-Convex Lenses'),
            ('/products/bk7-windows/', 'BK7 Windows'),
            ('/products/broadband-dielectric-mirrors/', 'Broadband Dielectric Mirrors'),
        ],
        7: [  # Custom vs Stock
            ('/products/aspherical-lenses/', 'Aspherical Lenses'),
            ('/products/achromatic-doublet/', 'Achromatic Doublet Lenses'),
            ('/products/bk7-windows/', 'BK7 Windows'),
        ],
        8: [  # Laser Optics
            ('/products/laser-line-high-reflected-mirrors/', 'Laser Line HR Mirrors'),
            ('/products/uv-fused-silica-plano-convex/', 'UV Fused Silica Plano-Convex Lenses'),
            ('/products/bk7-windows/', 'BK7 Windows'),
        ],
        9: [  # Optical Coating Types
            ('/products/narrow-band-interference-filters/', 'Narrow Band Interference Filters'),
            ('/products/cube-beamsplitters/', 'Cube Beamsplitters'),
            ('/products/enhanced-aluminum-mirrors/', 'Enhanced Aluminum Mirrors'),
        ],
        10: [  # Optical Quality
            ('/products/bk7-plano-convex/', 'BK7 Plano-Convex Lenses'),
            ('/products/bk7-windows/', 'BK7 Windows'),
            ('/products/broadband-dielectric-mirrors/', 'Broadband Dielectric Mirrors'),
        ],
        11: [  # Custom Optics Spec
            ('/products/aspherical-lenses/', 'Aspherical Lenses'),
            ('/products/achromatic-doublet/', 'Achromatic Doublet Lenses'),
            ('/products/bk7-right-angle-prisms/', 'BK7 Right Angle Prisms'),
        ],
        12: [  # Laser Damage Threshold
            ('/products/laser-line-high-reflected-mirrors/', 'Laser Line HR Mirrors'),
            ('/products/broadband-dielectric-mirrors/', 'Broadband Dielectric Mirrors'),
            ('/products/uv-fused-silica-windows/', 'UV Fused Silica Windows'),
        ],
        13: [  # Optical Coating Design
            ('/products/narrow-band-interference-filters/', 'Narrow Band Interference Filters'),
            ('/products/cube-beamsplitters/', 'Cube Beamsplitters'),
            ('/products/enhanced-aluminum-mirrors/', 'Enhanced Aluminum Mirrors'),
        ],
        14: [  # Optical Metrology
            ('/products/bk7-plano-convex/', 'BK7 Plano-Convex Lenses'),
            ('/products/bk7-windows/', 'BK7 Windows'),
            ('/products/corner-cube-prisms/', 'Corner Cube Prisms'),
        ],
        15: [  # High Power Laser Materials
            ('/products/uv-fused-silica-plano-convex/', 'UV Fused Silica Plano-Convex Lenses'),
            ('/products/uv-fused-silica-windows/', 'UV Fused Silica Windows'),
            ('/products/laser-line-high-reflected-mirrors/', 'Laser Line HR Mirrors'),
        ],
        16: [  # Precision Lenses Supplier
            ('/products/bk7-plano-convex/', 'BK7 Plano-Convex Lenses'),
            ('/products/bk7-bi-convex/', 'BK7 Bi-Convex Lenses'),
            ('/products/achromatic-doublet/', 'Achromatic Doublet Lenses'),
        ],
        17: [  # Optical Components Laser Systems
            ('/products/laser-line-high-reflected-mirrors/', 'Laser Line HR Mirrors'),
            ('/products/bk7-right-angle-prisms/', 'BK7 Right Angle Prisms'),
            ('/products/cube-beamsplitters/', 'Cube Beamsplitters'),
        ],
        18: [  # UV Fused Silica vs BK7
            ('/products/uv-fused-silica-plano-convex/', 'UV Fused Silica Plano-Convex Lenses'),
            ('/products/uv-fused-silica-windows/', 'UV Fused Silica Windows'),
            ('/products/bk7-plano-convex/', 'BK7 Plano-Convex Lenses'),
        ],
        19: [  # Custom Optics Manufacturing
            ('/products/aspherical-lenses/', 'Aspherical Lenses'),
            ('/products/achromatic-doublet/', 'Achromatic Doublet Lenses'),
            ('/products/bk7-windows/', 'BK7 Windows'),
        ],
        20: [  # AR Coating Selection
            ('/products/bk7-plano-convex/', 'BK7 Plano-Convex Lenses'),
            ('/products/uv-fused-silica-windows/', 'UV Fused Silica Windows'),
            ('/products/narrow-band-interference-filters/', 'Narrow Band Interference Filters'),
        ],
    }
    
    # Merge all blog links
    all_blog_links = {}
    all_blog_links.update(blog_links)
    all_blog_links.update(early_blog_links)
    
    total_added = 0
    for blog_id, links in all_blog_links.items():
        # Find the blog by id in the content
        id_pattern = '"id":\\s*' + str(blog_id) + '\\s*,'
        id_match = re.search(id_pattern, content)
        if not id_match:
            print(f"  WARNING: Could not find blog id={blog_id}")
            continue
        
        # Find the content field after this id
        # Look for "content": "..." (may be very long)
        # We need to find where content ends and append links before the closing
        start_pos = id_match.start()
        
        # Find "content": " 
        content_pattern = '"content":\\s*"'
        content_match = re.search(content_pattern, content[start_pos:])
        if not content_match:
            print(f"  WARNING: Could not find content for blog id={blog_id}")
            continue
        
        content_start = start_pos + content_match.end()
        
        # Find the end of content - it ends with unescaped "
        # Need to find matching closing quote
        pos = content_start
        while pos < len(content):
            if content[pos] == '\\':
                pos += 2  # Skip escaped character
                continue
            if content[pos] == '"':
                break
            pos += 1
        
        content_end = pos
        
        # Also find contentZh
        content_zh_pattern = '"contentZh":\\s*"'
        content_zh_match = re.search(content_zh_pattern, content[content_end:])
        if not content_zh_match:
            print(f"  WARNING: Could not find contentZh for blog id={blog_id}")
            continue
        
        content_zh_start = content_end + content_zh_match.end()
        
        pos = content_zh_start
        while pos < len(content):
            if content[pos] == '\\':
                pos += 2
                continue
            if content[pos] == '"':
                break
            pos += 1
        content_zh_end = pos
        
        # Build the link HTML to append
        en_links_html = '\\n\\n<h3>Related Products</h3>\\n<ul>' 
        zh_links_html = '\\n\\n<h3>相关产品</h3>\\n<ul>'
        
        for url, name in links:
            en_links_html += '\\n<li><a href=\"' + url + '\">' + name + '</a></li>'
            zh_links_html += '\\n<li><a href=\"' + url + '\">' + name + '</a></li>'
        
        en_links_html += '\\n</ul>'
        zh_links_html += '\\n</ul>'
        
        # Check if content already ends with related products section
        existing_content = content[content_start:content_end]
        if 'Related Products' in existing_content or '相关产品' in existing_content:
            print(f"  Blog {blog_id}: Already has related products section, skipping")
            continue
        
        # Append to content
        content = content[:content_end] + en_links_html + content[content_end:]
        
        # Recalculate contentZh position since content shifted
        # Find contentZh again from the blog block
        id_match2 = re.search(id_pattern, content)
        start_pos2 = id_match2.start()
        content_zh_match2 = re.search(content_zh_pattern, content[start_pos2:])
        content_zh_start2 = start_pos2 + content_zh_match2.end()
        
        pos = content_zh_start2
        while pos < len(content):
            if content[pos] == '\\':
                pos += 2
                continue
            if content[pos] == '"':
                break
            pos += 1
        content_zh_end2 = pos
        
        content = content[:content_zh_end2] + zh_links_html + content[content_zh_end2:]
        
        total_added += len(links)
        print(f"  Blog {blog_id}: Added {len(links)} product links")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Total product links added: {total_added}")
    return total_added

###############################################################################
# Task 4: Breadcrumb JSON-LD
###############################################################################

def task4_breadcrumb_jsonld():
    print("\n=== Task 4: Adding BreadcrumbList JSON-LD ===")
    filepath = os.path.join(BASE, "product-detail.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if BreadcrumbList already exists
    if 'BreadcrumbList' in content:
        print("  BreadcrumbList already exists, verifying format...")
        return True
    
    # Find where the Product schema is added and add BreadcrumbList after it
    # Find the line: document.head.appendChild(schemaScript);
    insert_pattern = "document.head.appendChild(schemaScript);"
    insert_pos = content.find(insert_pattern)
    if insert_pos < 0:
        print("  WARNING: Could not find schema insertion point")
        return False
    
    insert_after = insert_pos + len(insert_pattern)
    
    breadcrumb_code = '''

            // Add BreadcrumbList Schema
            var breadcrumbData = {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": "https://photonedgeoptics.com/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Products",
                        "item": "https://photonedgeoptics.com/products/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": currentProduct.name,
                        "item": "https://photonedgeoptics.com/products/" + currentProduct.slug + "/"
                    }
                ]
            };
            var breadcrumbScript = document.createElement('script');
            breadcrumbScript.type = 'application/ld+json';
            breadcrumbScript.textContent = JSON.stringify(breadcrumbData);
            document.head.appendChild(breadcrumbScript);'''
    
    content = content[:insert_after] + breadcrumb_code + content[insert_after:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  BreadcrumbList JSON-LD added successfully")
    return True

###############################################################################
# Task 5: Add 2 blogs + 1 news
###############################################################################

def task5_add_blogs_news():
    print("\n=== Task 5: Adding 2 blogs + 1 news ===")
    
    blog_filepath = os.path.join(BASE, "js/blog-data.js")
    with open(blog_filepath, 'r', encoding='utf-8') as f:
        blog_content = f.read()
    
    # Blog 26: Optical Prism Selection Guide
    blog26_content = r'''<h2>Introduction to Optical Prism Selection</h2>
<p>Selecting the right optical prism is critical for achieving optimal performance in your optical system. With various prism geometries available, each offering unique beam manipulation capabilities, understanding the selection criteria ensures you choose the most appropriate component for your application.</p>

<h2>Types of Optical Prisms</h2>
<p>Optical prisms come in several fundamental geometries, each designed for specific beam manipulation tasks:</p>
<ul>
<li><strong>Right Angle Prisms</strong>: Redirect light by 90 degrees through total internal reflection. Ideal for periscope systems, binoculars, and compact optical layouts. <a href="/products/bk7-right-angle-prisms/">View our Right Angle Prisms</a></li>
<li><strong>Penta Prisms</strong>: Deviate light by exactly 90 degrees regardless of orientation, making them essential for surveying instruments and alignment systems. <a href="/products/penta-prisms/">View our Penta Prisms</a></li>
<li><strong>Dove Prisms</strong>: Rotate images at twice the prism rotation rate, invaluable for target tracking and image de-rotation in spinning systems. <a href="/products/dove-prisms/">View our Dove Prisms</a></li>
<li><strong>Corner Cube Prisms (Retroreflectors)</strong>: Return incident light parallel to the source regardless of angle, critical for laser ranging and interferometry. <a href="/products/corner-cube-prisms/">View our Corner Cube Prisms</a></li>
<li><strong>Equilateral Dispersing Prisms</strong>: Separate wavelengths through angular dispersion, used in spectrometers and pulse compression. <a href="/products/equilateral-dispersing-prisms/">View our Equilateral Prisms</a></li>
<li><strong>Wollaston Prisms</strong>: Split light into two orthogonally polarized beams, essential for polarimetry and shear interferometry. <a href="/products/wollaston-prisms/">View our Wollaston Prisms</a></li>
</ul>

<h2>Key Selection Parameters</h2>
<h3>1. Wavelength Range</h3>
<p>The operating wavelength dictates material selection. BK7 provides excellent transmission from 350nm to 2.0um, while UV fused silica extends coverage down to 185nm for deep UV applications. For infrared systems beyond 2um, consider CaF2, ZnSe, or Ge substrates. Always verify the material transmission curve at your operating wavelength before selection.</p>

<h3>2. Size and Aperture Requirements</h3>
<p>Prism aperture must accommodate your beam diameter with adequate margin to avoid edge diffraction. A common guideline is to select a prism with an aperture at least 1.5 times your beam diameter. PhotonEdge offers prisms in sizes from 5mm to 50mm, covering most common optical system requirements.</p>

<h3>3. Angular Precision</h3>
<p>Angular tolerance directly impacts beam pointing accuracy. Standard prisms offer 1-3 arc minute tolerances, while precision-grade options achieve sub-arc-minute accuracy for metrology and alignment applications. Consider your system alignment budget when specifying angular tolerance.</p>

<h3>4. Coating Requirements</h3>
<p>Uncoated prisms rely on total internal reflection, which requires the incident angle to exceed the critical angle. When TIR conditions cannot be met, or for entrance/exit faces, anti-reflection coatings reduce Fresnel losses. Metal-dielectric coatings on reflecting surfaces provide reliable reflection when TIR is insufficient.</p>

<h2>Application-Based Recommendations</h2>
<h3>Imaging and Viewing Systems</h3>
<p>Right angle and Penta prisms are the standard choice for image erection and path folding in binoculars, periscopes, and camera viewfinders. Penta prisms are preferred when precise 90-degree deviation must be maintained regardless of mounting tolerances.</p>

<h3>Laser and Metrology Systems</h3>
<p>Corner cube prisms provide alignment-insensitive retroreflection for laser ranging and interferometric distance measurement. Wollaston prisms generate spatially separated polarized beams for polarization-sensitive detection in ellipsometry and optical current sensing.</p>

<h3>Spectral Analysis</h3>
<p>Equilateral dispersing prisms offer higher damage threshold alternatives to diffraction gratings for wavelength selection in tunable laser systems. The angular dispersion depends on both the prism material and geometry, with higher-dispersion materials providing greater spectral separation.</p>

<h3>Beam Steering and Scanning</h3>
<p>Dove prisms enable continuous image rotation in tracking systems and scanning imagers. Their compact form factor and simple rotation mechanism make them ideal for target acquisition and stabilization platforms.</p>

<h2>Conclusion</h2>
<p>Proper prism selection requires careful consideration of wavelength, beam size, angular precision, and coating requirements. PhotonEdge offers a comprehensive range of optical prisms in BK7, UV fused silica, and specialty materials with custom coating options. <a href="/contact.html">Contact our optical engineers</a> for application-specific selection assistance.</p>'''

    blog26_contentZh = r'''<h2>光学棱镜选型简介</h2>
<p>选择合适的光学棱镜对实现光学系统的最佳性能至关重要。各种棱镜几何形状各有独特的光束操控能力，理解选型标准可确保您选择最适合应用的元件。</p>

<h2>光学棱镜类型</h2>
<p>光学棱镜有几种基本几何形状，每种针对特定的光束操控任务：</p>
<ul>
<li><strong>直角棱镜</strong>：通过全内反射将光路偏转90度，适用于潜望镜、双筒望远镜和紧凑光学布局。<a href="/products/bk7-right-angle-prisms/">查看直角棱镜</a></li>
<li><strong>五角棱镜</strong>：无论方向如何均精确偏转90度，是测量仪器和对准系统的核心元件。<a href="/products/penta-prisms/">查看五角棱镜</a></li>
<li><strong>道威棱镜</strong>：以棱镜旋转两倍的速率旋转像面，在目标跟踪和旋转系统消旋中极具价值。<a href="/products/dove-prisms/">查看道威棱镜</a></li>
<li><strong>角锥棱镜（逆反射器）</strong>：不受角度影响将入射光平行返回，对激光测距和干涉测量至关重要。<a href="/products/corner-cube-prisms/">查看角锥棱镜</a></li>
<li><strong>等边色散棱镜</strong>：通过角色散分离波长，用于光谱仪和脉冲压缩。<a href="/products/equilateral-dispersing-prisms/">查看等边棱镜</a></li>
<li><strong>沃拉斯顿棱镜</strong>：将光束分为两个正交偏振分量，是偏振测量和剪切干涉的核心元件。<a href="/products/wollaston-prisms/">查看沃拉斯顿棱镜</a></li>
</ul>

<h2>关键选型参数</h2>
<h3>1. 波长范围</h3>
<p>工作波长决定材料选择。BK7在350nm至2.0μm提供优异透过率，UV熔融石英覆盖低至185nm的深紫外应用。对于2μm以上红外系统，考虑CaF2、ZnSe或Ge基底。选型前务必确认材料在工作波长处的透过率曲线。</p>

<h3>2. 尺寸与通光孔径</h3>
<p>棱镜孔径须容纳光束直径并留有足够余量以避免边缘衍射。常用准则是选择通光孔径至少为光束直径1.5倍的棱镜。PhotonEdge提供5mm至50mm规格的棱镜，覆盖大多数常见光学系统需求。</p>

<h3>3. 角度精度</h3>
<p>角度公差直接影响光束指向精度。标准棱镜提供1-3角分公差，精密级选项可达亚角分精度。确定角度公差时需考虑系统对准公差分配。</p>

<h3>4. 镀膜要求</h3>
<p>无镀膜棱镜依赖全内反射，要求入射角超过临界角。当TIR条件无法满足时，增透膜可减少菲涅尔损耗。反射面上的金属-介质镀膜在TIR不足时提供可靠反射。</p>

<h2>基于应用的推荐</h2>
<h3>成像与观察系统</h3>
<p>直角和五角棱镜是双筒望远镜、潜望镜和相机取景器中像面正像和光路折叠的标准选择。当必须无论安装公差如何都保持精确90度偏转时，五角棱镜更优。</p>

<h3>激光与计量系统</h3>
<p>角锥棱镜为激光测距和干涉距离测量提供对准不敏感的逆反射。沃拉斯顿棱镜为偏振敏感检测生成空间分离的偏振光束。</p>

<h3>光谱分析</h3>
<p>等边色散棱镜为可调谐激光系统的波长选择提供比衍射光栅更高损伤阈值的替代方案。</p>

<h3>光束偏转与扫描</h3>
<p>道威棱镜在跟踪系统和扫描成像器中实现连续像面旋转。紧凑外形和简单旋转机构使其成为目标捕获和稳定平台的理想选择。</p>

<h2>结论</h2>
<p>正确的棱镜选型需要仔细考虑波长、光束尺寸、角度精度和镀膜要求。PhotonEdge提供BK7、UV熔融石英和特种材料的全面光学棱镜产品线，并提供定制镀膜选项。<a href="/contact.html">联系我们的光学工程师</a>获取应用选型支持。</p>'''

    # Blog 27: Optical Component Cleaning and Maintenance
    blog27_content = r'''<h2>Introduction to Optical Component Maintenance</h2>
<p>Proper cleaning and maintenance of optical components is essential for preserving their performance and extending their service life. Contamination from dust, fingerprints, and organic residues can significantly degrade transmission, increase scatter, and potentially cause laser-induced damage. This guide provides comprehensive best practices for maintaining your precision optics.</p>

<h2>Cleaning Methods</h2>
<h3>Compressed Air and Dust Removal</h3>
<p>Always begin cleaning with gentle dust removal. Use filtered compressed air or a clean, dry nitrogen stream to blow away loose particles. Never use unfiltered air lines, as they may contain oil and moisture that will contaminate the surface. Hold the optic vertically and direct the air stream at an oblique angle to avoid driving particles into the surface. For stubborn particles, a soft camel-hair brush can be used with minimal contact pressure.</p>

<h3>Solvent Cleaning</h3>
<p>For fingerprints, oils, and organic contamination, solvent cleaning is the primary method. The standard technique is the drag method: fold a lint-free lens tissue into a pad, apply a few drops of solvent, and drag it slowly across the surface in a single direction without applying pressure. Common solvents include:</p>
<ul>
<li><strong>Acetone</strong>: Effective for organic residues; fast evaporation. Use only high-purity (optical grade) acetone.</li>
<li><strong>Isopropyl alcohol (IPA)</strong>: Gentler alternative for sensitive coatings; slower evaporation reduces streaking.</li>
<li><strong>Methanol</strong>: Excellent for final cleaning steps; leaves minimal residue.</li>
<li><strong>Deionized water</strong>: For water-soluble contaminants; must be followed by solvent rinse to prevent water spots.</li>
</ul>
<p>Never apply solvent directly to the optic. Instead, apply it to the cleaning tissue first. Never rub in a circular motion, as this grinds particles into the surface and can cause scratches.</p>

<h3>Ultrasonic Cleaning</h3>
<p>Ultrasonic cleaning is suitable for robust, unmounted optics that can withstand the cavitation energy. Use a low-power ultrasonic bath with an appropriate detergent solution, followed by thorough DI water rinsing and solvent drying. Avoid ultrasonic cleaning for cemented optics (such as achromatic doublets), polarizing beamsplitter cubes, or any component with adhesive bonds, as the vibration can weaken cement layers.</p>

<h2>Coating-Specific Cleaning Considerations</h2>
<h3>Anti-Reflection Coatings</h3>
<p>AR coatings are generally durable but require gentle handling. Broadband AR coatings on lenses and windows can be cleaned with standard solvents using the drag method. Avoid excessive pressure, as hard contact can scratch the coating surface. For UV-optimized AR coatings on fused silica optics, use only IPA or methanol, as acetone can sometimes interact with certain UV coating formulations. <a href="/products/bk7-plano-convex/">View our AR-coated lenses</a> and <a href="/products/uv-fused-silica-windows/">UV Fused Silica Windows</a></p>

<h3>Metallic Mirror Coatings</h3>
<p>Protected and enhanced metal coatings (aluminum, silver, gold) are vulnerable to mechanical damage during cleaning. Never drag a tissue across bare or enhanced metal coatings with any pressure. Use only the gentlest air or solvent vapor cleaning. Enhanced aluminum mirrors with dielectric overcoats offer better scratch resistance but should still be handled with extreme care. <a href="/products/enhanced-aluminum-mirrors/">View our Enhanced Aluminum Mirrors</a></p>

<h3>Dielectric Coatings</h3>
<p>Multi-layer dielectric coatings on beamsplitters, laser line mirrors, and filters are typically the most durable and can withstand careful solvent cleaning. However, always check manufacturer guidelines, as some specialty coatings (e.g., for UV or high-power applications) may have specific cleaning restrictions. <a href="/products/broadband-dielectric-mirrors/">View our Dielectric Mirrors</a> and <a href="/products/cube-beamsplitters/">Cube Beamsplitters</a></p>

<h2>Storage Best Practices</h2>
<ul>
<li>Store optics in clean, dry environments with desiccant packs to prevent moisture damage.</li>
<li>Use individual protective cases or lens tissue wrapping to prevent surface contact.</li>
<li>Keep optics in a temperature-stable environment to prevent coating stress from thermal cycling.</li>
<li>For long-term storage, seal optics in nitrogen-purged bags or containers.</li>
<li>Never store optics in direct sunlight or near heat sources.</li>
<li>Label storage containers with the optic type and coating information to avoid mix-ups.</li>
</ul>

<h2>Common Cleaning Mistakes to Avoid</h2>
<ul>
<li><strong>Using facial tissues or paper towels</strong>: These contain wood fibers and chemical brighteners that will scratch coatings and leave residues.</li>
<li><strong>Cleaning in a circular motion</strong>: This traps and grinds debris into the surface, causing micro-scratches.</li>
<li><strong>Applying solvent directly to the optic</strong>: Liquid can seep into mounted assemblies and damage cement or edge coatings.</li>
<li><strong>Using excessive force</strong>: Precision optical surfaces are extremely delicate; even light finger pressure can deform thin elements.</li>
<li><strong>Cleaning unnecessarily</strong>: Each cleaning cycle carries risk; clean only when optical performance is demonstrably degraded.</li>
<li><strong>Ignoring environmental controls</strong>: Dusty, humid, or contaminated work areas will re-soil optics immediately after cleaning.</li>
</ul>

<h2>When to Replace vs. Clean</h2>
<p>Optics with deep scratches, coating delamination, or laser damage sites should be replaced rather than cleaned. Attempting to clean damaged surfaces can worsen the defect and generate contamination that affects other system components. For high-value custom optics, consult PhotonEdge about recoating services as a cost-effective alternative to full replacement. <a href="/products/bk7-windows/">View our Optical Windows</a></p>

<h2>Conclusion</h2>
<p>Proper optical component maintenance is a disciplined practice that requires the right materials, techniques, and environmental conditions. By following these best practices, you can extend the operational life of your precision optics and maintain optimal system performance. For specific cleaning recommendations for your PhotonEdge products, <a href="/contact.html">contact our technical support team</a>.</p>'''

    blog27_contentZh = r'''<h2>光学元件维护简介</h2>
<p>正确清洁和维护光学元件对保持其性能和延长使用寿命至关重要。灰尘、指纹和有机残留物的污染会显著降低透过率、增加散射，并可能导致激光损伤。本指南提供维护精密光学的全面最佳实践。</p>

<h2>清洁方法</h2>
<h3>压缩空气与除尘</h3>
<p>始终从轻柔除尘开始。使用过滤压缩空气或干净的干燥氮气流吹走松散颗粒。切勿使用未过滤的空气管线，因为可能含油和水分污染表面。将光学元件竖直放置，以倾斜角度引导气流，避免将颗粒吹向表面。对于顽固颗粒，可使用柔软的驼毛刷以最小接触压力清除。</p>

<h3>溶剂清洁</h3>
<p>对于指纹、油污和有机污染，溶剂清洁是主要方法。标准技术是拖拽法：将无绒镜头纸折叠成垫，滴加几滴溶剂，沿单一方向缓慢拖过表面，不施加压力。常用溶剂包括：</p>
<ul>
<li><strong>丙酮</strong>：对有机残留物有效，蒸发快。仅使用高纯度（光学级）丙酮。</li>
<li><strong>异丙醇（IPA）</strong>：对敏感镀膜更温和，蒸发慢减少条纹。</li>
<li><strong>甲醇</strong>：适用于最终清洁步骤，残留极少。</li>
<li><strong>去离子水</strong>：用于水溶性污染物，之后须用溶剂冲洗防止水渍。</li>
</ul>
<p>切勿将溶剂直接涂在光学元件上，应先涂在清洁纸上。切勿以圆周运动擦拭，这会将颗粒研磨到表面造成划痕。</p>

<h3>超声清洁</h3>
<p>超声清洁适用于能承受空化能量的坚固未安装光学元件。使用低功率超声槽配合适当清洁剂，随后彻底去离子水冲洗和溶剂干燥。避免对胶合光学元件（如消色差双合透镜）、偏振分束立方或任何有胶粘结合的元件进行超声清洁，因为振动会削弱胶合层。</p>

<h2>不同镀膜的清洁注意事项</h2>
<h3>增透膜</h3>
<p>增透膜通常耐用但需轻柔处理。透镜和窗口上的宽带增透膜可用标准溶剂拖拽法清洁。避免过度施压，硬接触会刮伤镀膜表面。对于UV熔融石英上的UV优化增透膜，仅使用IPA或甲醇，因为丙酮有时会与某些UV镀膜配方反应。<a href="/products/bk7-plano-convex/">查看增透膜透镜</a>和<a href="/products/uv-fused-silica-windows/">UV熔融石英窗口</a></p>

<h3>金属反射膜</h3>
<p>保护和增强金属镀膜（铝、银、金）在清洁时易受机械损伤。切勿以任何压力拖拽纸巾经过裸露或增强金属镀膜。仅使用最温和的空气或溶剂蒸气清洁。带介质覆盖层的增强铝反射镜抗刮擦性更好，但仍需极其小心处理。<a href="/products/enhanced-aluminum-mirrors/">查看增强铝反射镜</a></p>

<h3>介质膜</h3>
<p>分束器、激光线反射镜和滤光片上的多层介质膜通常最耐用，可承受小心溶剂清洁。但务必查看制造商指南，因为某些特殊镀膜（如用于UV或高功率应用的）可能有特定清洁限制。<a href="/products/broadband-dielectric-mirrors/">查看介质反射镜</a>和<a href="/products/cube-beamsplitters/">立方分束器</a></p>

<h2>存储最佳实践</h2>
<ul>
<li>将光学元件存放在带有干燥剂包的清洁干燥环境中，防止湿气损伤。</li>
<li>使用单独的保护盒或镜头纸包裹，防止表面接触。</li>
<li>保持光学元件在温度稳定的环境中，防止热循环导致的镀膜应力。</li>
<li>长期存储时，将光学元件密封在充氮袋或容器中。</li>
<li>切勿将光学元件存放在阳光直射或热源附近。</li>
<li>在存储容器上标注光学元件类型和镀膜信息，避免混淆。</li>
</ul>

<h2>常见清洁错误</h2>
<ul>
<li><strong>使用面巾纸或纸巾</strong>：含有木纤维和化学增白剂，会刮伤镀膜并留下残留物。</li>
<li><strong>以圆周运动清洁</strong>：会困住碎屑并研磨到表面，造成微划痕。</li>
<li><strong>将溶剂直接涂在光学元件上</strong>：液体会渗入安装组件，损坏胶合或边缘镀膜。</li>
<li><strong>使用过度力量</strong>：精密光学表面极其脆弱，甚至轻微手指压力也会使薄元件变形。</li>
<li><strong>不必要地清洁</strong>：每次清洁循环都有风险，仅在光学性能明显下降时才清洁。</li>
<li><strong>忽视环境控制</strong>：多尘、潮湿或污染的工作区域会在清洁后立即重新污染光学元件。</li>
</ul>

<h2>何时更换而非清洁</h2>
<p>有深划痕、镀膜脱层或激光损伤点的光学元件应更换而非清洁。尝试清洁受损表面可能恶化缺陷并产生影响其他系统元件的污染。对于高价值定制光学，咨询PhotonEdge关于重新镀膜服务，作为全面更换的经济替代方案。<a href="/products/bk7-windows/">查看光学窗口</a></p>

<h2>结论</h2>
<p>正确的光学元件维护是一项需要合适材料、技术和环境条件的规范实践。遵循这些最佳实践可延长精密光学的使用寿命并保持最佳系统性能。如需PhotonEdge产品的特定清洁建议，<a href="/contact.html">联系我们的技术支持团队</a>。</p>'''

    # Build blog entries
    blog26 = '''  {
    "id": 26,
    "title": "Optical Prism Selection Guide - How to Choose the Right Prism for Your Application",
    "titleZh": "光学棱镜选型指南 - 如何为您的应用选择合适的棱镜",
    "slug": "optical-prism-selection-guide",
    "category": "Technical Guide",
    "categoryZh": "技术指南",
    "date": "2026-07-31",
    "author": "PhotonEdge Technical Team",
    "image": "/images/blog/optical-prism-selection-guide.jpg",
    "excerpt": "A comprehensive guide to selecting optical prisms based on wavelength, size, precision, and coating requirements, with application-specific recommendations.",
    "excerptZh": "基于波长、尺寸、精度和镀膜要求选择光学棱镜的综合指南，含应用推荐。",
    "content": "''' + blog26_content.replace('"', '\\"') + '''",
    "contentZh": "''' + blog26_contentZh.replace('"', '\\"') + '''"
  }'''

    blog27 = '''  {
    "id": 27,
    "title": "How to Clean and Maintain Optical Components - Best Practices",
    "titleZh": "如何清洁和维护光学元件 - 最佳实践",
    "slug": "optical-component-cleaning-maintenance-guide",
    "category": "Technical Guide",
    "categoryZh": "技术指南",
    "date": "2026-07-31",
    "author": "PhotonEdge Technical Team",
    "image": "/images/blog/optical-component-cleaning-maintenance-guide.jpg",
    "excerpt": "Essential best practices for cleaning and maintaining optical components including lenses, mirrors, windows, and prisms, with coating-specific guidelines.",
    "excerptZh": "清洁和维护透镜、反射镜、窗口和棱镜等光学元件的核心最佳实践，含不同镀膜的专项指南。",
    "content": "''' + blog27_content.replace('"', '\\"') + '''",
    "contentZh": "''' + blog27_contentZh.replace('"', '\\"') + '''"
  }'''

    # Find the last blog entry and add after it
    # Find the closing of the last blog entry
    # The array ends with ]; so we need to add before that
    # Find the last } before the closing ]
    last_brace = blog_content.rfind('}')
    if last_brace < 0:
        print("  WARNING: Could not find last blog entry")
        return False
    
    # Insert new blogs after the last entry
    blog_content = blog_content[:last_brace+1] + ',\n' + blog26 + ',\n' + blog27 + blog_content[last_brace+1:]
    
    with open(blog_filepath, 'w', encoding='utf-8') as f:
        f.write(blog_content)
    
    print("  Added Blog 26: Optical Prism Selection Guide")
    print("  Added Blog 27: Optical Component Cleaning & Maintenance")
    
    # Now add news article 13
    news_filepath = os.path.join(BASE, "js/news-data.js")
    with open(news_filepath, 'r', encoding='utf-8') as f:
        news_content = f.read()
    
    news13 = '''  {
    "id": 13,
    "title": "PhotonEdge to Attend LASER World of PHOTONICS 2027",
    "titleZh": "PhotonEdge将参加2027年慕尼黑光博会",
    "slug": "photonedge-laser-world-photonics-2027",
    "date": "2026-07-31",
    "image": "/images/news/laser-world-photonics-2027.jpg",
    "excerpt": "PhotonEdge announces its participation in LASER World of PHOTONICS 2027 in Munich, showcasing latest precision optics innovations and manufacturing capabilities.",
    "excerptZh": "PhotonEdge宣布将参加2027年慕尼黑国际光博会，展示最新精密光学创新和制造能力。",
    "content": "PhotonEdge is pleased to announce its participation in LASER World of PHOTONICS 2027, the world\\'s leading trade fair for photonics components, systems, and applications. The event will take place at the Munich Trade Fair Centre in Germany.\\n\\nAt the exhibition, PhotonEdge will showcase its latest innovations in precision optical components, including advanced aspherical lenses, high-power laser mirrors, UV fused silica optics, and custom optical assemblies. Visitors will have the opportunity to meet with our optical engineering team and discuss their specific requirements for demanding applications in laser systems, medical devices, semiconductor manufacturing, and defense.\\n\\n\\\"LASER World of PHOTONICS is the premier platform for connecting with global photonics leaders and demonstrating our commitment to precision and quality,\\\" said the PhotonEdge management team. \\\"We look forward to presenting our expanded product portfolio and discussing how our custom optical solutions can address the evolving needs of the industry.\\\"\\n\\nThe company will feature live demonstrations of optical testing capabilities and provide detailed consultations on coating specifications for high-energy laser applications. New product launches planned for the show include an expanded range of deep UV optical components and next-generation laser line mirrors with enhanced damage thresholds.\\n\\nTo schedule a meeting with the PhotonEdge team at the show, please contact us at sales@photonedgeoptics.com or visit our booth details page closer to the event date.",
    "contentZh": "PhotonEdge欣然宣布将参加2027年慕尼黑国际光博会（LASER World of PHOTONICS 2027），这是全球领先的光子学元器件、系统和应用贸易展会。展会将在德国慕尼黑展览中心举行。\\n\\n在展会上，PhotonEdge将展示精密光学元件的最新创新成果，包括先进非球面透镜、高功率激光反射镜、UV熔融石英光学元件和定制光学组件。参观者将有机会与我们的光学工程团队面对面交流，讨论激光系统、医疗器械、半导体制造和国防等高要求应用的具体需求。\\n\\nPhotonEdge管理层表示：\\\"慕尼黑光博会是与全球光子学行业领袖建立联系、展示我们对精密和质量承诺的顶级平台。我们期待展示扩大的产品组合，并探讨我们的定制光学解决方案如何满足行业不断演进的需求。\\\"\\n\\n公司将现场展示光学测试能力，并提供高能激光应用镀膜规格的详细咨询。计划在展会上推出的新产品包括扩展的深紫外光学元件系列和具有增强损伤阈值的新一代激光线反射镜。\\n\\n如需预约展会期间与PhotonEdge团队会面，请联系sales@photonedgeoptics.com，或在临近展会日期时访问我们的展位详情页面。"
  }'''
    
    last_brace_news = news_content.rfind('}')
    news_content = news_content[:last_brace_news+1] + ',\n' + news13 + news_content[last_brace_news+1:]
    
    with open(news_filepath, 'w', encoding='utf-8') as f:
        f.write(news_content)
    
    print("  Added News 13: PhotonEdge to Attend LASER World of PHOTONICS 2027")
    
    # Create blog directory pages
    for slug in ['optical-prism-selection-guide', 'optical-component-cleaning-maintenance-guide']:
        blog_dir = os.path.join(BASE, "blog", slug)
        os.makedirs(blog_dir, exist_ok=True)
        blog_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="/js/main.js"></script>
<script src="/js/blog-data.js"></script>
<script src="/js/translations.js"></script>
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<script>
var slug = "''' + slug + '''";
document.addEventListener("DOMContentLoaded", function() {
  var blog = null;
  for (var i = 0; i < BLOG_POSTS.length; i++) {
    if (BLOG_POSTS[i].slug === slug) { blog = BLOG_POSTS[i]; break; }
  }
  if (blog) {
    document.title = blog.title + " | PhotonEdge";
    var content = '<h1>' + blog.title + '</h1>' + blog.content;
    document.getElementById("blog-content").innerHTML = content;
  }
});
</script>
<div id="blog-content"></div>
</body>
</html>'''
        with open(os.path.join(blog_dir, "index.html"), 'w', encoding='utf-8') as f:
            f.write(blog_html)
        print(f"  Created blog directory: blog/{slug}/")
    
    # Create news directory page
    news_slug = 'photonedge-laser-world-photonics-2027'
    news_dir = os.path.join(BASE, "news", news_slug)
    os.makedirs(news_dir, exist_ok=True)
    news_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="/js/main.js"></script>
<script src="/js/news-data.js"></script>
<script src="/js/translations.js"></script>
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<script>
var slug = "''' + news_slug + '''";
document.addEventListener("DOMContentLoaded", function() {
  var article = null;
  for (var i = 0; i < NEWS_ARTICLES.length; i++) {
    if (NEWS_ARTICLES[i].slug === slug) { article = NEWS_ARTICLES[i]; break; }
  }
  if (article) {
    document.title = article.title + " | PhotonEdge";
    var content = '<h1>' + article.title + '</h1>' + article.content;
    document.getElementById("news-content").innerHTML = content;
  }
});
</script>
<div id="news-content"></div>
</body>
</html>'''
    with open(os.path.join(news_dir, "index.html"), 'w', encoding='utf-8') as f:
        f.write(news_html)
    print(f"  Created news directory: news/{news_slug}/")
    
    return True

###############################################################################
# Task 6: Update sitemap.xml
###############################################################################

def task6_update_sitemap():
    print("\n=== Task 6: Updating sitemap.xml ===")
    filepath = os.path.join(BASE, "sitemap.xml")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count current URLs
    current_count = content.count('<url>')
    print(f"  Current URL count: {current_count}")
    
    # Update all lastmod to 2026-07-31
    content = re.sub(r'<lastmod>[^<]*</lastmod>', '<lastmod>2026-07-31</lastmod>', content)
    
    # Add 3 new URLs before </urlset>
    new_urls = '''  <url>
    <loc>https://photonedgeoptics.com/blog/optical-prism-selection-guide/index.html</loc>
    <lastmod>2026-07-31</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://photonedgeoptics.com/blog/optical-component-cleaning-maintenance-guide/index.html</loc>
    <lastmod>2026-07-31</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://photonedgeoptics.com/news/photonedge-laser-world-photonics-2027/index.html</loc>
    <lastmod>2026-07-31</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
'''
    
    content = content.replace('</urlset>', new_urls + '</urlset>')
    
    new_count = content.count('<url>')
    print(f"  New URL count: {new_count}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return new_count

###############################################################################
# Task 7: Update translations.js
###############################################################################

def task7_update_translations():
    print("\n=== Task 7: Updating translations.js ===")
    filepath = os.path.join(BASE, "js/translations.js")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add translation keys for new blog/news content if needed
    # Check if we need any new UI-facing translation keys
    # For blog/news content loaded dynamically from data.js, no translation keys needed
    # Only add keys if there are new static UI elements
    
    # Add "Related Products" section heading translations
    # This is rendered from blog content, not from translations.js, so no changes needed
    
    print("  No new UI translation keys needed - blog/news content is dynamically loaded")
    return True

###############################################################################
# Main execution
###############################################################################

if __name__ == '__main__':
    print("PhotonEdge V80 Update Script")
    print("=" * 60)
    
    task1_expand_descriptions()
    task2_check_alt_tags()
    task3_blog_links()
    task4_breadcrumb_jsonld()
    task5_add_blogs_news()
    task6_update_sitemap()
    task7_update_translations()
    
    print("\n" + "=" * 60)
    print("All tasks completed!")

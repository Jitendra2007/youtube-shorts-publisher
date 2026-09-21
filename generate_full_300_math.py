"""
Comprehensive Generator for the 30-Day Master Mathematics Curriculum (300 Equations).
Populates all 30 days with complete metadata for video rendering.
"""

import os
import json

ALL_300_EQUATIONS = []

# Raw Data Definition for 30 Days (10 Equations per day = 300 items)
RAW_CURRICULUM_DATA = [
    # =========================================================================
    # DAY 01: Grade 7 Basic Geometry & Measurements
    # =========================================================================
    (1, "Grade 7", [
        ("Area of a Circle", "A = pi * r^2", "Archimedes of Syracuse (c. 250 BC)", "nature", "beat_pulse", "nature_history_lofi",
         "Have you ever wondered why multiplying pi by the radius squared gives the exact area of any circular object in the universe?",
         "Over twenty-two hundred years ago, ancient Greek genius Archimedes proved that slicing a circle into infinite tiny triangles creates a rectangle of area pi r squared.",
         "Its purpose is to calculate the two-dimensional surface space enclosed inside any curved round shape using the universal constant pi.",
         "Used constantly by civil engineers for pipe waterflow, aerospace engineers designing satellite dishes, and pizza restaurants sizing their pans.",
         "Every circle in nature follows this rule. Like this video and subscribe to our channel for equation number two tomorrow!"),
        ("Circumference of a Circle", "C = 2 * pi * r", "Archimedes & Ancient Geometers (c. 250 BC)", "nature", "ken_burns", "nature_history_lofi",
         "How do engineers calculate the exact outer boundary distance of a giant Ferris wheel without stretching a giant tape measure around it?",
         "Ancient geometers discovered that if you unroll any circle into a straight line, its length is always exactly two times pi times its radius.",
         "Its purpose is to measure the complete perimeter or outer boundary length of any circular object.",
         "Essential for designing car tire rotations, speedometer calibration, running tracks, and planetary orbit perimeters.",
         "From your watch to planetary orbits, circumference rules rotation. Subscribe to our channel for our next equation!"),
        ("Area of a Triangle", "Area = (1/2) * Base * Height", "Euclid of Alexandria (c. 300 BC)", "abstract", "glitch_pop", "space_tech",
         "Why does half base times height give the area of every single triangle, no matter how skewed or sharp its angles are?",
         "In three hundred BC, Euclid proved in his Elements that any triangle is precisely one-half of a surrounding parallelogram with the same base and height.",
         "Its purpose is to measure planar surface areas of three-sided polygons by reducing them to rectangular halves.",
         "Powers 3D video game graphics rasterization, roof truss architecture, bridge engineering, and land surveying.",
         "Every 3D video game world is made of triangles using this formula. Like and subscribe to master all 300 equations!"),
        ("Area of a Rectangle", "Area = Length * Breadth", "Ancient Egyptian Land Surveyors (c. 2000 BC)", "abstract", "ken_burns", "nature_history_lofi",
         "What is the very first fundamental formula that founded modern civilization, agriculture, and property ownership?",
         "Four thousand years ago, ancient Nile surveyors needed to recalculate farmland boundaries after annual river floods, giving birth to length times breadth.",
         "Its purpose is to quantify two-dimensional surface space divided into equal square units.",
         "Used in calculating room flooring tiles, solar panel surface absorption, real estate valuations, and silicon microchip layouts.",
         "Every screen pixel and apartment floor uses this formula. Hit like and subscribe to our channel for daily equations!"),
        ("Perimeter of a Rectangle", "P = 2 * (Length + Breadth)", "Babylonian Builders (c. 1800 BC)", "nature", "beat_pulse", "nature_history_lofi",
         "How do farmers know the exact length of fencing wire needed to enclose a vast rectangular boundary without measuring every single step?",
         "Babylonian architects utilized the sum of lengths and breadths doubled to construct city walls and perimeter defenses.",
         "Its purpose is to measure the total outer boundary around a rectangular area.",
         "Used for property fencing, running track markings, picture frame borders, and stadium security perimeters.",
         "Simple math secures real-world boundaries. Like and subscribe for our 30-day mathematics marathon!"),
        ("Area of a Parallelogram", "Area = Base * Perpendicular Height", "Euclid of Alexandria (c. 300 BC)", "abstract", "glitch_pop", "space_tech",
         "What happens when you tilt a rectangle sideways? Does its total surface area change or remain identical?",
         "Euclid proved that shifting a rectangle into a slanted parallelogram preserves its exact area as long as its perpendicular height remains constant.",
         "Its purpose is to calculate skewed quadrilateral areas by projecting their true perpendicular heights.",
         "Crucial for solar panel tilt efficiency, civil road cross-sections, and mechanical linkage physics.",
         "Geometry proves that tilting shapes preserves their core essence. Subscribe to our channel for more math secrets!"),
        ("Area of a Trapezium", "Area = (1/2) * (a + b) * h", "Archimedes of Syracuse (c. 225 BC)", "nature", "ken_burns", "nature_history_lofi",
         "How do engineers calculate the volume of concrete in a tapered dam or canal bank with unequal parallel sides?",
         "Archimedes showed that averaging the two parallel bases and multiplying by height yields the exact trapezoid area.",
         "Its purpose is to calculate irregular four-sided areas that taper between two parallel boundary lines.",
         "Used in river channel waterflow volume calculations, airplane wing cross-sections, and highway embankments.",
         "From mega-dams to stealth aircraft wings, the trapezoid area rules fluid design. Like and subscribe for more!"),
        ("Sum of Angles in a Triangle", "Angle A + Angle B + Angle C = 180 deg", "Pythagoras & Thales (c. 550 BC)", "space", "beat_pulse", "space_tech",
         "Did you know that regardless of whether a triangle is tiny as an atom or massive as a galaxy, its interior angles always add up to exactly 180 degrees?",
         "Six centuries before Christ, ancient Greek mathematicians proved that parallel lines lock a triangle's interior angles at a straight line.",
         "Its purpose is to establish the flat Euclidean nature of two-dimensional geometric space.",
         "Used in triangulating GPS satellite positions, celestial astronomy telescope alignments, and surveyor theodolites.",
         "One hundred eighty degrees is the eternal law of flat space. Subscribe to our channel for equation number nine!"),
        ("Supplementary Angles Identity", "Angle 1 + Angle 2 = 180 deg", "Euclid of Alexandria (c. 300 BC)", "abstract", "glitch_pop", "space_tech",
         "What simple law ensures that a straight road or laser beam never bends unless an external force deflects it?",
         "Euclid established that two adjacent angles forming a straight linear pair must sum to exactly one hundred eighty degrees.",
         "Its purpose is to define straight lines and calculate unknown deflection angles across intersecting planes.",
         "Used in robotic arm joint articulation, laser beam mirrors, CNC cutting machines, and railway track switching.",
         "Straight lines define modern robotics. Like this video and subscribe to unlock all 300 mathematics equations!"),
        ("Speed, Distance and Time", "Distance = Speed * Time", "Galileo Galilei (1638)", "space", "ken_burns", "space_tech",
         "How does Google Maps predict your exact minute of arrival across hundreds of miles of highway traffic?",
         "In sixteen thirty-eight, Galileo Galilei formalized kinematic motion: Distance traversed equals velocity multiplied by duration.",
         "Its purpose is to connect physical movement through space to the flow of time.",
         "Powers aircraft autopilot cruisers, rocket orbital burn durations, GPS navigation, and high-speed rail schedules.",
         "This concludes Day One fundamentals! Subscribe to our channel for Day Two as we explore arithmetic and commercial math!")
    ]),

    # =========================================================================
    # DAY 02: Grade 7 Arithmetic, Percentages & Commercial Math
    # =========================================================================
    (2, "Grade 7", [
        ("Simple Interest Formula", "I = (P * R * T) / 100", "Renaissance Bankers (c. 1500)", "nature", "beat_pulse", "nature_history_lofi",
         "How do banks determine the exact fee charged when you borrow money or save in a fixed deposit account?",
         "Renaissance Italian merchant banks created the simple interest equation to standardize loans based on principal, rate, and time.",
         "Its purpose is to calculate linear financial growth on invested capital over fixed durations.",
         "Used for auto loans, basic personal lending, government bonds, and fixed bank deposits.",
         "Understanding interest is the first step to financial freedom. Like and subscribe for more banking math!"),
        ("Percentage Calculation Formula", "Percentage = (Part / Whole) * 100", "Ancient Roman Tax Collectors (c. 50 BC)", "abstract", "glitch_pop", "space_tech",
         "Why is the number one hundred used across the entire world to compare exam scores, battery levels, and discounts?",
         "Ancient Romans calculated taxes per hundred units, creating percentum, which evolved into modern percentage.",
         "Its purpose is to normalize fractions into a standardized scale of one hundred for direct comparison.",
         "Powers smartphone battery indicators, stock market percentage gains, retail sale discounts, and exam grades.",
         "From phone batteries to discounts, percentage rules daily metrics. Subscribe to our channel for equation thirteen!"),
        ("Profit and Loss Equation", "Profit = Selling Price - Cost Price", "Luca Pacioli (Father of Accounting, 1494)", "nature", "ken_burns", "nature_history_lofi",
         "What is the single mathematical equation that determines whether a corner store or a multi-billion dollar tech company survives or dies?",
         "In fourteen ninety-four, Italian mathematician Luca Pacioli published double-entry bookkeeping, formalizing Profit equals Selling Price minus Cost Price.",
         "Its purpose is to measure net economic gain or loss in any financial trade or commerce transaction.",
         "Powers corporate quarterly earnings, e-commerce pricing engines, stock valuation models, and crypto trades.",
         "Every business on Earth runs on Pacioli's profit equation. Like and subscribe to our channel for more!"),
        ("Profit Percentage", "Profit % = (Profit / Cost Price) * 100", "Venetian Traders (c. 1500)", "abstract", "beat_pulse", "nature_history_lofi",
         "Why is making ten dollars profit on a hundred dollar item vastly better than making ten dollars on a million dollar item?",
         "Venetian spice merchants standardized profit percentage to measure return on capital investment accurately.",
         "Its purpose is to evaluate return on investment efficiency relative to capital spent.",
         "Used in stock ROI metrics, e-commerce profit margin analysis, and venture capital startup assessments.",
         "Profit margin separates smart investments from bad ones. Subscribe for our daily math journey!"),
        ("Discount and Marked Price Formula", "Discount % = (Discount / Marked Price) * 100", "Modern Retail Economists (c. 1850)", "nature", "glitch_pop", "nature_history_lofi",
         "How do online shopping algorithms calculate flash sale discounts and dynamic price drops in milliseconds?",
         "Nineteenth-century department stores formalized marked price minus selling price to incentivize mass retail consumer sales.",
         "Its purpose is to calculate price reductions relative to original catalog retail list prices.",
         "Used in Black Friday discounts, e-commerce coupon engines, and airline ticket dynamic pricing algorithms.",
         "Smart shopping begins with discount math. Like this video and subscribe to our channel!"),
        ("Direct Proportion Ratio", "y / x = k  (or y = k * x)", "Euclid & Eudoxus (c. 350 BC)", "space", "ken_burns", "space_tech",
         "If five apples cost ten dollars, how does your brain instantly know that ten apples cost twenty dollars without writing code?",
         "Greek mathematician Eudoxus formulated proportionality theory, proving that when one variable doubles, its paired variable doubles identically.",
         "Its purpose is to model linear scaling where two quantities maintain a constant ratio k.",
         "Used in recipe scaling, currency exchange rates, speedometer distance ratios, and 3D architectural model scales.",
         "Direct proportions scale the universe. Subscribe to our channel for equation seventeen!"),
        ("Inverse Proportion Relationship", "x * y = k", "Robert Boyle & Edme Mariotte (1662)", "abstract", "beat_pulse", "space_tech",
         "If ten workers build a wall in four days, why do twenty workers build it in two days instead of eight days?",
         "Physicist Robert Boyle formalized inverse proportionality in sixteen sixty-two when proving that gas volume decreases as pressure increases.",
         "Its purpose is to model systems where increasing one factor causes a proportional decrease in another factor.",
         "Used in workforce project scheduling, gas cylinder compression physics, gear ratio transmission, and camera aperture shutter speeds.",
         "More speed means less time - the beauty of inverse proportion. Like and subscribe for more math!"),
        ("Unitary Method Equation", "Unit Value = Total Cost / Quantity", "Medieval Indian & Arab Merchants (c. 800 AD)", "nature", "glitch_pop", "nature_history_lofi",
         "What is the universal mental shortcut every person on earth uses to compare grocery supermarket bargains?",
         "Medieval silk route merchants formalized finding the cost of a single unit first before multiplying by desired quantities.",
         "Its purpose is to determine unit costs to enable rapid scaling for any arbitrary quantity.",
         "Powers grocery unit pricing labels, cloud server compute cost per hour, and fuel mileage economy calculations.",
         "The unitary method is the master key to smart shopping. Hit like and subscribe to our channel!"),
        ("Average (Arithmetic Mean)", "Mean = Sum of Items / Number of Items", "Pythagoras & Ancient Statisticians (c. 500 BC)", "abstract", "ken_burns", "space_tech",
         "How do climate scientists summarize millions of temperature measurements across an entire continent into a single meaningful number?",
         "Ancient Greek Pythagoreans introduced the arithmetic mean as the perfect balance point among varying numeric quantities.",
         "Its purpose is to calculate the central tendency of a collection of numeric values.",
         "Used in cricket batting averages, national GDP per capita, machine learning data normalization, and student grade point averages.",
         "Averages balance big data across the globe. Subscribe to our channel for tomorrow's equation!"),
        ("Ratio and Fraction Equivalence", "a / b = c / d  =>  a * d = b * c", "Euclid of Alexandria (c. 300 BC)", "space", "beat_pulse", "space_tech",
         "Why does cross-multiplying two fractions instantly prove whether they are equal or reveal missing variables?",
         "Euclid proved in Book Five of his Elements that the product of the extremes equals the product of the means in any proportion.",
         "Its purpose is to solve unknown terms in geometric proportions and algebraic fractions.",
         "Used in medical drug dosage scaling, chemical stoichiometry reactions, and CAD engineering scaling.",
         "That finishes Day Two! Like and subscribe for Day Three as we master exponents, powers, and number theory!")
    ]),

    # =========================================================================
    # DAY 03: Grade 8 Exponents, Powers & Number Theory
    # =========================================================================
    (3, "Grade 8", [
        ("Product Rule of Exponents", "a^m * a^n = a^(m + n)", "René Descartes & John Wallis (1655)", "abstract", "beat_pulse", "space_tech",
         "How do computers multiply gigabytes and terabytes of binary data in nanoseconds without running out of memory?",
         "In sixteen thirty-seven, René Descartes invented modern exponential notation, proving that multiplying powers with equal bases means adding their exponents.",
         "Its purpose is to simplify rapid multiplication of repeated factors into basic exponent addition.",
         "Powers computer RAM sizing, binary processing, cryptographic key length calculations, and astronomical distance notation.",
         "Exponents power the digital computing revolution. Like and subscribe to our channel for more!"),
        ("Quotient Rule of Exponents", "a^m / a^n = a^(m - n)", "John Wallis & Isaac Newton (1676)", "abstract", "glitch_pop", "space_tech",
         "What simple law lets astrophysicists divide astronomical distances like light years without writing hundreds of zeros?",
         "English mathematician John Wallis formalized fractional exponents, proving that dividing powers subtracts their exponents.",
         "Its purpose is to simplify large-scale division into straightforward exponent subtraction.",
         "Used in signal-to-noise ratio decibel measurements, radioactive decay half-life calculations, and Richter earthquake scales.",
         "From earthquake scales to sound decibels, exponents simplify giant numbers. Subscribe for more!"),
        ("Power of a Power Rule", "(a^m)^n = a^(m * n)", "René Descartes (1637)", "space", "ken_burns", "space_tech",
         "Why does raising two to the third power and then squaring the result equal two to the sixth power?",
         "Descartes demonstrated that nesting exponential powers collapses cleanly into multiplying exponents together.",
         "Its purpose is to calculate exponential growth rates and multi-layered dimensional transformations.",
         "Used in 3D voxel graphics scaling, quantum state multiplicity, and compound interest compounding cycles.",
         "Multiplying powers creates hyper-fast computational growth. Like and subscribe for equation twenty-four!"),
        ("Zero Exponent Identity", "a^0 = 1  (for a != 0)", "Nicolas Chuquet (1484)", "abstract", "beat_pulse", "nature_history_lofi",
         "Why does any number on Earth, whether it is five or nine trillion, equal exactly ONE when raised to the power of zero?",
         "French mathematician Nicolas Chuquet showed that dividing a number by itself creates an exponent difference of zero, proving a to the power zero equals one.",
         "Its purpose is to preserve consistency across the laws of algebra and multiplication identities.",
         "Powers computer floating-point math libraries, calculus polynomials, and combinatorics base cases.",
         "Zero exponent is algebra's ultimate reset button. Subscribe to our channel for more math gems!"),
        ("Negative Exponent Rule", "a^(-n) = 1 / a^n", "John Wallis (1655)", "nature", "glitch_pop", "space_tech",
         "What does a negative exponent really mean? Does it make a number negative, or does it shrink it into a microscopic fraction?",
         "John Wallis proved that negative powers represent repeated division, flipping the number under a fraction line.",
         "Its purpose is to represent infinitesimal scientific scales like nanometers and microvolts cleanly.",
         "Used in chemistry pH scales for acidity, semiconductor nanometer dimensions, and radio frequency wavelengths.",
         "Negative exponents reveal the microscopic atomic universe. Like and subscribe for more!"),
        ("Scientific Notation Standard", "N = m * 10^k  (1 <= m < 10)", "Archimedes & John Napier (1614)", "space", "ken_burns", "space_tech",
         "How do NASA scientists write the mass of the Sun, which is a two followed by thirty zeros, on a small computer display?",
         "Archimedes first counted grains of sand in the universe using powers of ten, leading to modern scientific notation.",
         "Its purpose is to standardize extremely massive astronomical numbers and ultra-tiny atomic dimensions.",
         "Used in astrophysics telescope software, GPS atomic clock synchronization, and quantum physics constants.",
         "Scientific notation measures from galaxies to atoms. Subscribe for equation twenty-seven!"),
        ("Square of a Sum Algebraic Identity", "(a + b)^2 = a^2 + 2*a*b + b^2", "Euclid of Alexandria (c. 300 BC)", "abstract", "beat_pulse", "nature_history_lofi",
         "Why does squaring a plus b create that mysterious extra two a b in the middle instead of just a squared plus b squared?",
         "Euclid proved geometrically in his Elements that subdividing a large square with side a plus b leaves two smaller squares and two identical rectangles of area a b.",
         "Its purpose is to expand binomial squares rapidly without manual term-by-term foil multiplication.",
         "Powers quadratic optimization in machine learning, signal processing filtering, and architectural engineering.",
         "Geometry explains why the middle two a b term exists. Like this video and subscribe to our channel!"),
        ("Square of a Difference Identity", "(a - b)^2 = a^2 - 2*a*b + b^2", "Euclid of Alexandria (c. 300 BC)", "abstract", "glitch_pop", "space_tech",
         "What is the secret algebra rule used to calculate variance and standard deviation in artificial intelligence data science?",
         "Ancient Greek geometers derived this by subtracting overlapping rectangles from a larger square area.",
         "Its purpose is to expand squared algebraic differences and quantify error margins in mathematics.",
         "Powers Mean Squared Error loss functions in machine learning AI, statistical variance, and regression modeling.",
         "Machine learning AI trains itself using squared differences. Subscribe for equation twenty-nine!"),
        ("Difference of Two Squares Identity", "a^2 - b^2 = (a - b) * (a + b)", "Euclid & Diophantus (c. 250 AD)", "space", "ken_burns", "space_tech",
         "How can you instantly calculate ninety-nine times one hundred one in your head in less than two seconds?",
         "Greek mathematician Diophantus proved that multiplying a minus b by a plus b perfectly cancels the middle cross-terms.",
         "Its purpose is to factorize difference of squares and perform rapid mental arithmetic shortcuts.",
         "Used in RSA cryptography factorization, quantum mechanics matrix commutators, and high-frequency trading calculations.",
         "One hundred squared minus one is ninety-nine ninety-nine - pure math magic! Like and subscribe for more!"),
        ("Compound Interest Formula", "A = P * (1 + r/n)^(n*t)", "Jacob Bernoulli (1683)", "nature", "beat_pulse", "nature_history_lofi",
         "Why did Albert Einstein reportedly call compound interest the eighth wonder of the world?",
         "In sixteen eighty-three, Swiss mathematician Jacob Bernoulli studied continuous financial compounding, which led directly to the discovery of the constant e.",
         "Its purpose is to calculate exponential wealth generation where interest earns interest over time.",
         "Drives retirement 401k funds, stock market compounding, cryptocurrency staking yields, and bank mortgages.",
         "Compound interest transforms small savings into immense fortunes. Subscribe for Day Four as we dive into linear equations!")
    ])
]

# Generate standard template for all remaining days (Days 4 to 30)
DAYS_TOPICS = [
    # (Day, Level, [(Name, Formula, Founder, Category, Motion, BGM, Hook, Purpose, Apps)])
    (4, "Grade 8", [
        ("Linear Equation in One Variable", "a*x + b = 0  =>  x = -b/a", "Al-Khwarizmi (820 AD)", "space", "beat_pulse", "space_tech", "How do computers solve unknown variables in budgets?", "Solves linear unknowns.", "Used in balance sheets and sensors."),
        ("Sum of Interior Angles of Polygon", "Sum = (n - 2) * 180 deg", "Euclid (300 BC)", "abstract", "glitch_pop", "space_tech", "What is the angle sum inside a 20-sided polygon?", "Calculates polygon interior angles.", "Used in 3D CAD modeling."),
        ("Regular Polygon Interior Angle", "Angle = ((n - 2) * 180) / n", "Euclid (300 BC)", "nature", "ken_burns", "nature_history_lofi", "Why are honeycombs made of perfect hexagons?", "Determines corner angles.", "Used in tile tessellations."),
        ("Sum of Exterior Angles of Polygon", "Sum = 360 deg", "Thales of Miletus (580 BC)", "space", "beat_pulse", "space_tech", "Why does walking around any polygon turn you 360 degrees?", "Proves angular boundary closure.", "Used in robot pathfinding."),
        ("Area of a Rhombus", "Area = (1/2) * d1 * d2", "Archimedes (250 BC)", "nature", "glitch_pop", "nature_history_lofi", "How do you find diamond area from diagonals?", "Calculates area using diagonals.", "Used in gemstone cutting."),
        ("Volume of a Cuboid", "V = Length * Breadth * Height", "Archimedes (250 BC)", "abstract", "ken_burns", "space_tech", "How does Amazon calculate cargo container space?", "Measures 3D rectangular box volume.", "Used in global logistics."),
        ("Total Surface Area of a Cuboid", "TSA = 2 * (lb + bh + hl)", "Archimedes (250 BC)", "nature", "beat_pulse", "nature_history_lofi", "How much cardboard is needed to make a box?", "Calculates external surface skin.", "Used in packaging manufacturing."),
        ("Volume of a Cube", "V = a^3", "Archimedes (250 BC)", "abstract", "glitch_pop", "space_tech", "Why does doubling width make a box hold 8x water?", "Quantifies cubic space scaling.", "Used in Minecraft voxel engines."),
        ("Lateral Surface Area of a Cuboid", "LSA = 2 * h * (l + b)", "Babylonian Builders (1800 BC)", "nature", "ken_burns", "nature_history_lofi", "How do painters calculate wall paint needed?", "Calculates 4 perimeter walls.", "Used in wallpaper estimation."),
        ("Euler's Polyhedral Formula", "V - E + F = 2", "Leonhard Euler (1758)", "space", "beat_pulse", "space_tech", "Why do all 3D solid shapes equal two in this formula?", "Defines topological invariants.", "Used in 3D game meshes.")
    ]),
    (5, "Grade 8", [
        ("Classical Probability Formula", "P(E) = n(E) / n(S)", "Pascal & Fermat (1654)", "abstract", "beat_pulse", "space_tech", "How do casinos predict future odds with certainty?", "Calculates event likelihood.", "Used in weather and casino odds."),
        ("Probability Complement Rule", "P(Not E) = 1 - P(E)", "Laplace (1812)", "space", "glitch_pop", "space_tech", "If rain is 30%, why is sunshine exactly 70%?", "Finds probability of non-occurrence.", "Used in cyber defense risk."),
        ("Range of a Data Set", "Range = Max - Min", "John Graunt (1662)", "nature", "ken_burns", "nature_history_lofi", "How do meteorologists measure temperature volatility?", "Measures numeric dispersion.", "Used in stock volatility."),
        ("Class Mark of Interval", "Class Mark = (Upper + Lower) / 2", "Adolphe Quetelet (1835)", "abstract", "beat_pulse", "space_tech", "How do statisticians find histogram center points?", "Finds interval midpoints.", "Used in census demographic data."),
        ("Distance on 1D Number Line", "d = |x2 - x1|", "René Descartes (1637)", "nature", "glitch_pop", "nature_history_lofi", "Why is mathematical distance always positive?", "Measures 1D coordinate separation.", "Used in audio amplitude."),
        ("Midpoint on 1D Line", "Midpoint = (x1 + x2) / 2", "Descartes (1637)", "space", "ken_burns", "space_tech", "Where is the balance point between two real numbers?", "Finds exact bisection.", "Used in binary search logic."),
        ("Direct Variation Constant", "k = y / x", "Eudoxus (350 BC)", "abstract", "beat_pulse", "space_tech", "How do engineers calibrate rocket fuel flow?", "Measures linear scaling factor.", "Used in Hooke's elasticity law."),
        ("Inverse Variation Constant", "k = x * y", "Robert Boyle (1662)", "nature", "glitch_pop", "nature_history_lofi", "Why does higher speed decrease travel time?", "Maintains product invariance.", "Used in camera aperture stops."),
        ("Pythagorean Triplet Generator", "a = m^2-n^2, b = 2mn, c = m^2+n^2", "Brahmagupta (628 AD)", "space", "ken_burns", "space_tech", "How to generate infinite integer right triangles?", "Generates integer solutions.", "Used in CAD rasterization."),
        ("Volume of Right Circular Cylinder", "V = pi * r^2 * h", "Archimedes (250 BC)", "abstract", "beat_pulse", "space_tech", "How do factories design soda cans for 350ml?", "Calculates cylinder volume.", "Used in engines and fuel tanks.")
    ]),
    (6, "Grade 9", [
        ("2D Coordinate Distance Formula", "d = sqrt((x2-x1)^2 + (y2-y1)^2)", "René Descartes (1637)", "space", "beat_pulse", "space_tech", "How does phone GPS measure your distance to a taxi?", "Measures Euclidean distance.", "Used in GPS and video games."),
        ("Section Formula Internal Division", "x = (mx2+nx1)/(m+n)", "Descartes & Apollonius (1637)", "abstract", "glitch_pop", "space_tech", "How does animation software interpolate character paths?", "Divides line in m:n ratio.", "Used in CGI animation splines."),
        ("2D Midpoint Formula", "M = ((x1+x2)/2, (y1+y2)/2)", "Descartes (1637)", "nature", "ken_burns", "nature_history_lofi", "How do video games position cameras between players?", "Finds center 2D coordinate.", "Used in game camera framing."),
        ("Centroid of a Triangle", "G = ((x1+x2+x3)/3, (y1+y2+y3)/3)", "Archimedes (250 BC)", "space", "beat_pulse", "space_tech", "What point lets a triangle balance on a pencil tip?", "Finds center of mass.", "Used in aircraft balancing."),
        ("Area of Triangle by Coordinates", "Area = (1/2)|x1(y2-y3)+x2(y3-y1)+x3(y1-y2)|", "Gauss (1799)", "abstract", "glitch_pop", "space_tech", "How do satellites calculate farmland areas from GPS?", "Calculates polygon area from vertices.", "Used in GIS land mapping."),
        ("Collinearity Condition of 3 Points", "x1(y2-y3)+x2(y3-y1)+x3(y1-y2) = 0", "Descartes (1637)", "nature", "ken_burns", "nature_history_lofi", "How does radar verify if 3 targets are in a straight line?", "Tests collinear alignment.", "Used in missile guidance."),
        ("Slope of a Line through 2 Points", "m = (y2 - y1) / (x2 - x1)", "Descartes (1637)", "space", "beat_pulse", "space_tech", "How do engineers test if mountain roads are too steep?", "Measures rise over run.", "Used in highway design and stocks."),
        ("Point-Slope Form of a Line", "y - y1 = m * (x - x1)", "Descartes (1637)", "abstract", "glitch_pop", "space_tech", "How do games calculate bullet flight paths?", "Defines line from point and slope.", "Used in game ballistics."),
        ("Two-Point Form of a Line", "(y-y1)/(y2-y1) = (x-x1)/(x2-x1)", "Descartes (1637)", "nature", "ken_burns", "nature_history_lofi", "How do charts plot shortest flight routes?", "Connects two points linearly.", "Used in aviation navigation."),
        ("General Linear Equation 2 Variables", "Ax + By + C = 0", "Descartes (1637)", "space", "beat_pulse", "space_tech", "What formula encompasses all straight lines?", "Universal 2D linear form.", "Used in linear programming.")
    ]),
    (7, "Grade 9-10", [
        ("The Quadratic Formula", "x = (-b +- sqrt(b^2-4ac)) / 2a", "Brahmagupta & Al-Khwarizmi (628 AD)", "abstract", "beat_pulse", "space_tech", "How do scientists calculate artillery touch-down time?", "Solves quadratic polynomials.", "Used in rocket ballistics."),
        ("Discriminant of Quadratic Equation", "Delta = b^2 - 4ac", "Gauss (1801)", "space", "glitch_pop", "space_tech", "How to know root types without solving?", "Tests quadratic root nature.", "Used in resonance stability."),
        ("Sum of Roots of Quadratic", "alpha + beta = -b / a", "Viète (1579)", "nature", "ken_burns", "nature_history_lofi", "How are roots linked directly to coefficients?", "Connects roots to linear terms.", "Used in electrical impedance."),
        ("Product of Roots of Quadratic", "alpha * beta = c / a", "Viète (1579)", "abstract", "beat_pulse", "space_tech", "What locks root multiplication to the constant term?", "Connects roots to constant terms.", "Used in signal filtering."),
        ("Quadratic Formation from Roots", "x^2 - (Sum)x + (Product) = 0", "Viète (1579)", "space", "glitch_pop", "space_tech", "How do sound engineers build audio filters?", "Builds equations from roots.", "Used in audio equalization."),
        ("Remainder Theorem for Polynomials", "f(a) = Remainder of f(x)/(x-a)", "Bézout (1779)", "nature", "ken_burns", "nature_history_lofi", "How to find polynomial remainder in one step?", "Evaluates remainders instantly.", "Used in CRC error detection."),
        ("Factor Theorem for Polynomials", "If f(a)=0 then (x-a) is factor", "Descartes (1637)", "abstract", "beat_pulse", "space_tech", "How do computer algebra systems factor equations?", "Proves exact divisibility.", "Used in cryptographic solvers."),
        ("Cubic Algebraic Identity", "(a+b)^3 = a^3+3a^2b+3ab^2+b^3", "Nicomachus (100 AD)", "space", "glitch_pop", "space_tech", "Why does 3D cube expansion create prisms and rods?", "Expands cubic binomials.", "Used in thermodynamics state laws."),
        ("Sum of Two Cubes Factorization", "a^3+b^3 = (a+b)(a^2-ab+b^2)", "Al-Karaji (1000 AD)", "nature", "ken_burns", "nature_history_lofi", "How to factor sum of cubes effortlessly?", "Factorizes cubic terms.", "Used in elliptic curve crypto."),
        ("Difference of Two Cubes Factorization", "a^3-b^3 = (a-b)(a^2+ab+b^2)", "Al-Karaji (1000 AD)", "space", "beat_pulse", "space_tech", "What identity simplifies volume differentials?", "Factorizes difference of cubes.", "Used in engine fluid dynamics.")
    ]),
    (8, "Grade 10", [
        ("Sine Definition in Right Triangle", "sin(theta) = Opposite / Hypotenuse", "Aryabhata (499 AD)", "abstract", "beat_pulse", "space_tech", "How did ancient astronomers calculate planet distances?", "Defines vertical elevation ratio.", "Used in radio waves and GPS."),
        ("Cosine Definition in Right Triangle", "cos(theta) = Adjacent / Hypotenuse", "Al-Battani (880 AD)", "space", "glitch_pop", "space_tech", "How does radar determine horizontal position?", "Defines horizontal base ratio.", "Used in 3D graphics lighting."),
        ("Tangent Definition in Right Triangle", "tan(theta) = Opposite / Adjacent", "Abu al-Wafa (970 AD)", "nature", "ken_burns", "nature_history_lofi", "How to measure Mount Everest height without climbing?", "Measures slope ratio.", "Used in surveying theodolites."),
        ("Pythagorean Trigonometric Identity", "sin^2(theta) + cos^2(theta) = 1", "Hipparchus (150 BC)", "space", "beat_pulse", "space_tech", "Why does sin squared plus cos squared always equal one?", "Locks functions to unit circle.", "Used in AC power grids and AI."),
        ("Secant-Tangent Trigonometric Identity", "1 + tan^2(theta) = sec^2(theta)", "Abu al-Wafa (970 AD)", "abstract", "glitch_pop", "space_tech", "How do engineers convert slopes to line-of-sight?", "Relates slopes to secant.", "Used in raytracing engines."),
        ("Cosecant-Cotangent Identity", "1 + cot^2(theta) = csc^2(theta)", "Al-Battani (920 AD)", "nature", "ken_burns", "nature_history_lofi", "What governs reciprocal wave harmonics?", "Relates cotangent to cosecant.", "Used in sound dampening."),
        ("Complementary Angle Sine-Cosine Identity", "sin(90 - theta) = cos(theta)", "Aryabhata (499 AD)", "space", "beat_pulse", "space_tech", "Why does sin 30 equal cos 60 exactly?", "Connects complementary angles.", "Used in coordinate rotations."),
        ("Tangent-Sine-Cosine Relationship", "tan(theta) = sin(theta) / cos(theta)", "Al-Battani (880 AD)", "abstract", "glitch_pop", "space_tech", "How do video games compute climbing slopes?", "Expresses slope as velocity ratio.", "Used in vehicle physics."),
        ("Values of Special Trigonometric Angles", "sin(30)=1/2, sin(45)=1/sqrt(2), sin(60)=sqrt(3)/2", "Ptolemy (150 AD)", "nature", "ken_burns", "nature_history_lofi", "Why are 30, 45, 60 angles everywhere in blueprints?", "Standard exact closed-form values.", "Used in solar panel angles."),
        ("Height and Distance Elevation Formula", "Height = Distance * tan(Angle)", "Al-Biruni (1020 AD)", "space", "beat_pulse", "space_tech", "How did Al-Biruni calculate Earth radius 1000 years ago?", "Finds height via elevation.", "Used in satellite altimetry.")
    ]),
    (9, "Grade 10", [
        ("Curved Surface Area of a Cylinder", "CSA = 2 * pi * r * h", "Archimedes (250 BC)", "nature", "beat_pulse", "nature_history_lofi", "How much metal wraps a jumbo jet fuselage?", "Calculates cylindrical skin.", "Used in fuselage design."),
        ("Total Surface Area of a Cylinder", "TSA = 2 * pi * r * (r + h)", "Archimedes (250 BC)", "abstract", "glitch_pop", "space_tech", "How to calculate chemical tank protective coating?", "Includes endcaps and side skin.", "Used in battery cell casings."),
        ("Curved Surface Area of a Cone", "CSA = pi * r * l", "Archimedes (250 BC)", "nature", "ken_burns", "nature_history_lofi", "How do tent makers size camping tepees?", "Calculates lateral cone area.", "Used in megaphone acoustics."),
        ("Slant Height of a Cone", "l = sqrt(r^2 + h^2)", "Pythagoras & Archimedes (250 BC)", "space", "beat_pulse", "space_tech", "How do rocket engineers size nose cones?", "Finds conical slope length.", "Used in aerodynamic nose cones."),
        ("Volume of a Cone", "V = (1/3) * pi * r^2 * h", "Democritus & Archimedes (400 BC)", "abstract", "glitch_pop", "space_tech", "Why does a cone hold 1/3 of a cylinder's volume?", "Measures tapered 3D volume.", "Used in grain silos and volcanoes."),
        ("Surface Area of a Sphere", "A = 4 * pi * r^2", "Archimedes (225 BC)", "space", "ken_burns", "space_tech", "Why is a sphere's area 4x its shadow circle?", "Calculates 3D sphere area.", "Used in planetary atmosphere radiation."),
        ("Volume of a Sphere", "V = (4/3) * pi * r^3", "Archimedes (225 BC)", "nature", "beat_pulse", "nature_history_lofi", "How do astronomers calculate planet masses?", "Measures internal 3D capacity.", "Used in astrophysics and bubbles."),
        ("Area of a Circle Sector", "Area = (theta / 360) * pi * r^2", "Archimedes (250 BC)", "abstract", "glitch_pop", "space_tech", "How do radar sweeps calculate fractional area?", "Measures circular slice area.", "Used in radar sweep cones."),
        ("Length of an Arc of a Circle", "Arc Length = (theta / 360) * 2 * pi * r", "Archimedes (250 BC)", "space", "ken_burns", "space_tech", "How to calculate turning train track curve length?", "Measures curve segment length.", "Used in railway road bends."),
        ("Frustum of a Cone Volume", "V = (1/3)*pi*h*(r1^2+r2^2+r1*r2)", "Heron (100 AD)", "nature", "beat_pulse", "nature_history_lofi", "How to calculate drinking glass liquid capacity?", "Calculates truncated cone volume.", "Used in rocket exhaust nozzles.")
    ]),
    (10, "Grade 10", [
        ("Arithmetic Progression n-th Term", "a_n = a + (n - 1)*d", "Gauss & Brahmagupta (628 AD)", "abstract", "beat_pulse", "space_tech", "How to predict loan payments 20 years away?", "Calculates terms with constant diff.", "Used in loan repayment schedules."),
        ("Sum of First n Terms of AP", "S_n = (n / 2) * (2a + (n - 1)*d)", "Gauss (1787)", "space", "glitch_pop", "space_tech", "How did 10-year-old Gauss sum 1 to 100 in 5 seconds?", "Sums linear progressions.", "Used in depreciation accounting."),
        ("Alternate AP Sum Formula", "S_n = (n / 2) * (First + Last)", "Gauss (1787)", "nature", "ken_burns", "nature_history_lofi", "Fast shortcut to sum evenly spaced numbers?", "Averages endpoints multiplied by n.", "Used in high-frequency trading."),
        ("Arithmetic Mean of 2 Numbers", "AM = (a + b) / 2", "Pythagoras (500 BC)", "abstract", "beat_pulse", "space_tech", "Where is the balance point between two values?", "Finds intermediate balance.", "Used in temperature averaging."),
        ("Geometric Progression n-th Term", "a_n = a * r^(n - 1)", "Euclid (300 BC)", "space", "glitch_pop", "space_tech", "How does a viral video infect millions in days?", "Calculates exponential growth terms.", "Used in viral social algorithms."),
        ("Sum of First n Terms of GP", "S_n = a * (r^n - 1) / (r - 1)", "Euclid (300 BC)", "nature", "ken_burns", "nature_history_lofi", "How do pension funds project compound stock sums?", "Sums finite geometric series.", "Used in pension fund compounding."),
        ("Sum of Infinite Geometric Series", "S_inf = a / (1 - r)  (|r|<1)", "Archimedes & Euler (1734)", "space", "beat_pulse", "space_tech", "How can adding infinite fractions equal TWO?", "Sums shrinking infinite terms.", "Used in fractal geometry and DSP."),
        ("Geometric Mean of 2 Numbers", "GM = sqrt(a * b)", "Pythagoras (500 BC)", "abstract", "glitch_pop", "space_tech", "Why do stock investors use geometric mean for CAGR?", "Calculates multiplicative center.", "Used in investment portfolio CAGR."),
        ("AM-GM Inequality", "(a + b)/2 >= sqrt(a * b)", "Cauchy (1821)", "nature", "ken_burns", "nature_history_lofi", "Why is arithmetic average always >= geometric average?", "Fundamental inequality bound.", "Used in mathematical optimization."),
        ("Harmonic Mean Formula", "HM = (2 * a * b) / (a + b)", "Pythagoras & Archytas (400 BC)", "space", "beat_pulse", "space_tech", "Why is roundtrip average speed NOT simple average?", "Calculates true rate average.", "Used in parallel resistors & F1 score.")
    ]),
    (11, "Grade 10-11", [
        ("Trigonometric Law of Sines", "a / sin(A) = b / sin(B) = c / sin(C)", "Al-Battani (920 AD)", "abstract", "beat_pulse", "space_tech", "How do ships navigate stormy seas without right angles?", "Solves non-right triangles.", "Used in marine GPS navigation."),
        ("Trigonometric Law of Cosines", "c^2 = a^2 + b^2 - 2ab*cos(C)", "Al-Kashi (1420 AD)", "space", "glitch_pop", "space_tech", "What is the ultimate generalized Pythagorean theorem?", "Relates 3 sides and any angle.", "Used in robotic arm inverse kinematics."),
        ("Heron's Formula for Triangle Area", "A = sqrt(s(s-a)(s-b)(s-c))", "Heron of Alexandria (60 AD)", "nature", "ken_burns", "nature_history_lofi", "How to find triangle area with ZERO angles known?", "Calculates area from side lengths.", "Used in land surveyor plot sizing."),
        ("Semi-Perimeter of a Triangle", "s = (a + b + c) / 2", "Heron (60 AD)", "abstract", "beat_pulse", "space_tech", "What is the key geometric variable in polygon circles?", "Calculates half boundary perimeter.", "Used in incircle and excircle math."),
        ("Sine Addition Formula", "sin(A + B) = sinA*cosB + cosA*sinB", "Ptolemy & Euler (1748)", "space", "glitch_pop", "space_tech", "How do wireless cell towers combine radio signals?", "Expands angular frequencies.", "Used in Wi-Fi and 5G modulation."),
        ("Cosine Addition Formula", "cos(A + B) = cosA*cosB - sinA*sinB", "Ptolemy & Euler (1748)", "nature", "ken_burns", "nature_history_lofi", "Why does cosine addition subtract cross terms?", "Combines rotational angles.", "Used in aircraft flight dynamics."),
        ("Tangent Addition Formula", "tan(A + B) = (tanA + tanB)/(1 - tanA*tanB)", "Euler (1748)", "abstract", "beat_pulse", "space_tech", "How do civil engineers calculate road junction curves?", "Sums angular slopes.", "Used in highway interchange curves."),
        ("Double Angle Sine Identity", "sin(2*theta) = 2*sin(theta)*cos(theta)", "Abu al-Wafa (970 AD)", "space", "glitch_pop", "space_tech", "How do sound synthesizers double octave frequencies?", "Calculates harmonic frequency doubles.", "Used in music synthesizers."),
        ("Double Angle Cosine Identity", "cos(2*theta) = cos^2(theta) - sin^2(theta)", "Abu al-Wafa (970 AD)", "nature", "ken_burns", "nature_history_lofi", "What identity powers electric motor AC oscillations?", "Converts squared waves to 2x freq.", "Used in electric motor drives."),
        ("Double Angle Tangent Identity", "tan(2*theta) = (2*tan(theta))/(1 - tan^2(theta))", "Abu al-Wafa (970 AD)", "abstract", "beat_pulse", "space_tech", "How do optical mirrors double laser deflection angles?", "Doubles angular trajectory slopes.", "Used in laser galvo scanners.")
    ]),
    (12, "Grade 10-11", [
        ("Standard Equation of a Circle", "(x - h)^2 + (y - k)^2 = r^2", "Apollonius & Descartes (1637)", "space", "beat_pulse", "space_tech", "How do radar displays map circular airspace boundaries?", "Defines 2D circle with center (h,k).", "Used in air traffic radar bubbles."),
        ("General Equation of a Circle", "x^2 + y^2 + 2gx + 2fy + c = 0", "Descartes (1637)", "abstract", "glitch_pop", "space_tech", "What algebraic formula encompasses every circle?", "Expanded general circle form.", "Used in 2D collision detection."),
        ("Circle Center & Radius", "Center = (-g, -f), Radius = sqrt(g^2+f^2-c)", "Descartes (1637)", "nature", "ken_burns", "nature_history_lofi", "How to extract circle center and radius in 1 step?", "Extracts geometric parameters.", "Used in computer vision detection."),
        ("Tangent to Circle at (x1, y1)", "x*x1 + y*y1 = r^2", "Apollonius (200 BC)", "space", "beat_pulse", "space_tech", "How does a bicycle wheel touch the flat road at 1 point?", "Calculates tangent line equation.", "Used in vehicle tire grip modeling."),
        ("Slope Form of Circle Tangent", "y = m*x +- r*sqrt(1 + m^2)", "Descartes (1637)", "abstract", "glitch_pop", "space_tech", "How to find parallel tangent lines at any slope?", "Constructs tangent from slope m.", "Used in optics raytracing."),
        ("Length of Tangent from Point", "L = sqrt(x1^2 + y1^2 - r^2)", "Euclid & Apollonius (200 BC)", "nature", "ken_burns", "nature_history_lofi", "How far can a lookout on a ship see before horizon curves?", "Calculates tangent distance.", "Used in nautical horizon distance."),
        ("Power of a Point Theorem", "PA * PB = PT^2", "Jakob Steiner (1826)", "space", "beat_pulse", "space_tech", "Why do intersecting circle secants have equal products?", "Relates intersecting chords & tangents.", "Used in optical lens design."),
        ("Incircle Radius of a Triangle", "r = Area / s", "Heron (60 AD)", "abstract", "glitch_pop", "space_tech", "How to find radius of the largest circle inside a triangle?", "Calculates inscribed circle radius.", "Used in mechanical gear bearings."),
        ("Circumcircle Radius of a Triangle", "R = (a * b * c) / (4 * Area)", "Ptolemy (150 AD)", "nature", "ken_burns", "nature_history_lofi", "How to draw a circle passing through 3 cities?", "Calculates circumscribed radius.", "Used in cell tower coverage grids."),
        ("Radical Axis of Two Circles", "S1 - S2 = 0", "Gaspard Monge (1800)", "space", "beat_pulse", "space_tech", "What straight line shares equal tangent power for 2 circles?", "Defines equal power locus line.", "Used in computer graphics morphing.")
    ]),
    (13, "Grade 11", [
        ("Complex Number Standard Form", "z = a + i*b  (where i^2 = -1)", "Rafael Bombelli (1572)", "abstract", "beat_pulse", "space_tech", "Why did mathematicians invent imaginary numbers?", "Extends 1D numbers to 2D plane.", "Used in AC electrical circuits and quantum physics."),
        ("Modulus of a Complex Number", "|z| = sqrt(a^2 + b^2)", "Argand & Gauss (1806)", "space", "glitch_pop", "space_tech", "How to measure magnitude in the complex plane?", "Measures distance from origin.", "Used in signal power amplitude."),
        ("Argument (Phase) of Complex Number", "theta = arctan(b / a)", "Euler & Argand (1777)", "nature", "ken_burns", "nature_history_lofi", "What angle governs complex AC electrical phase shifts?", "Measures rotational phase angle.", "Used in radio phase modulation."),
        ("Polar Form of a Complex Number", "z = r * (cos(theta) + i*sin(theta))", "Euler (1748)", "space", "beat_pulse", "space_tech", "How to convert numbers into pure rotations?", "Expresses numbers in radius & angle.", "Used in radar phasor diagrams."),
        ("Euler's Complex Exponential Form", "z = r * e^(i * theta)", "Leonhard Euler (1748)", "abstract", "glitch_pop", "space_tech", "What is the most elegant equation in complex algebra?", "Unifies exponentials & rotations.", "Used in quantum wave mechanics."),
        ("De Moivre's Theorem", "(cos(theta) + i*sin(theta))^n = cos(n*theta) + i*sin(n*theta)", "Abraham de Moivre (1707)", "nature", "ken_burns", "nature_history_lofi", "How to raise complex numbers to the 100th power instantly?", "Multiplies angles when powering.", "Used in signal filtering and roots."),
        ("Cube Roots of Unity Identity", "1 + omega + omega^2 = 0", "Euler (1770)", "space", "beat_pulse", "space_tech", "Why do the three cube roots of 1 form a perfect triangle?", "Sum of symmetric unity roots is zero.", "Used in 3-phase electrical power."),
        ("Complex Conjugate Identity", "z * conjugate(z) = |z|^2", "Gauss (1831)", "abstract", "glitch_pop", "space_tech", "Why does multiplying a number by its conjugate eliminate i?", "Yields real squared magnitude.", "Used in quantum probability amplitudes."),
        ("Triangle Inequality for Complex Numbers", "|z1 + z2| <= |z1| + |z2|", "Cauchy (1821)", "nature", "ken_burns", "nature_history_lofi", "Why is a straight line always shorter than a detour?", "Bounds magnitude of vector sums.", "Used in signal noise limits."),
        ("Section Formula for Complex Coordinates", "z = (m*z2 + n*z1) / (m + n)", "Argand (1806)", "space", "beat_pulse", "space_tech", "How do graphics engines interpolate in 2D complex plane?", "Calculates weighted segment points.", "Used in Bezier curve spline generation.")
    ]),
    (14, "Grade 11", [
        ("Permutations Formula", "nPr = n! / (n - r)!", "Pascal & Euler (1654)", "abstract", "beat_pulse", "space_tech", "How many PIN codes can be made from 10 digits?", "Counts ordered arrangements.", "Used in password security encryption."),
        ("Combinations Formula", "nCr = n! / (r! * (n - r)!)", "Pascal & Fermat (1654)", "space", "glitch_pop", "space_tech", "How many unique lottery lottery tickets exist in a 6/49 game?", "Counts unordered selections.", "Used in lottery odds and genomics."),
        ("Pascal's Combinatorial Identity", "nCr + nC(r-1) = (n+1)Cr", "Blaise Pascal (1653)", "nature", "ken_burns", "nature_history_lofi", "What rule generates the famous Pascal's Triangle?", "Sums adjacent combination terms.", "Used in genetics probability grids."),
        ("Binomial Theorem Expansion", "(a + b)^n = sum(nCr * a^(n-r) * b^r)", "Sir Isaac Newton (1665)", "space", "beat_pulse", "space_tech", "How did Newton expand any power of binomials?", "Expands n-th degree polynomials.", "Used in financial derivatives pricing."),
        ("General Term in Binomial Expansion", "T_(r+1) = nCr * a^(n-r) * b^r", "Newton (1665)", "abstract", "glitch_pop", "space_tech", "How to find the 50th term without expanding all 100?", "Locates specific polynomial terms.", "Used in statistical series approximations."),
        ("Sum of Binomial Coefficients", "sum(nCr, r=0..n) = 2^n", "Pascal (1653)", "nature", "ken_burns", "nature_history_lofi", "Why is the total number of all subsets always 2 to the n?", "Sums all possible combination sizes.", "Used in digital logic power sets."),
        ("Circular Permutations Formula", "Arrangements = (n - 1)!", "Arthur Cayley (1850)", "space", "beat_pulse", "space_tech", "How many ways can 10 people sit around a circular table?", "Accounts for rotational symmetry.", "Used in circular network routing."),
        ("Derangements (Subfactorial) Formula", "!n = n! * sum((-1)^k / k!)", "Pierre Raymond de Montmort (1708)", "abstract", "glitch_pop", "space_tech", "What are the odds that no one in Secret Santa gets their own gift?", "Counts permutations with zero fixed points.", "Used in randomized cryptographic hashing."),
        ("Pigeonhole Principle Bound", "If n items > k boxes, at least 1 box has >= 2", "Peter Gustav Dirichlet (1834)", "nature", "ken_burns", "nature_history_lofi", "Why must at least two people in London have equal hair counts?", "Guarantees collision in finite bins.", "Used in hash collision proofs and crypto."),
        ("Multinomial Coefficient Formula", "n! / (n1! * n2! * ... * nk!)", "Leibniz (1695)", "space", "beat_pulse", "space_tech", "How many unique anagrams can be formed from MISSISSIPPI?", "Arranges sets with repeated items.", "Used in DNA sequence permutation analysis.")
    ]),
    (15, "Grade 11", [
        ("Standard Parabola Equation", "y^2 = 4*a*x", "Menaechmus & Apollonius (200 BC)", "abstract", "beat_pulse", "space_tech", "Why are all satellite dishes shaped like parabolas?", "Focuses parallel incoming rays to 1 point.", "Used in satellite dishes and headlights."),
        ("Focus and Directrix of Parabola", "Focus = (a, 0), Directrix: x = -a", "Apollonius (200 BC)", "space", "glitch_pop", "space_tech", "What geometric rule defines every parabolic curve?", "Equal distance to point and line.", "Used in solar concentrators."),
        ("Standard Ellipse Equation", "x^2 / a^2 + y^2 / b^2 = 1", "Apollonius & Kepler (1609)", "nature", "ken_burns", "nature_history_lofi", "Why do all planets orbit the Sun in ellipses?", "Defines oval curve with 2 foci.", "Used in Kepler's laws of planetary orbits."),
        ("Eccentricity of an Ellipse", "e = sqrt(1 - b^2 / a^2)", "Johannes Kepler (1609)", "space", "beat_pulse", "space_tech", "How do astronomers measure how stretched a comet orbit is?", "Measures elongation from circle.", "Used in satellite orbit transfer design."),
        ("Foci of an Ellipse", "Foci = (+- a*e, 0)", "Kepler (1609)", "abstract", "glitch_pop", "space_tech", "Why can whispering at one spot in a dome be heard at another?", "Focal points reflect sound perfectly.", "Used in whispering gallery architecture."),
        ("Standard Hyperbola Equation", "x^2 / a^2 - y^2 / b^2 = 1", "Apollonius (200 BC)", "nature", "ken_burns", "nature_history_lofi", "What curve shapes sonic booms and nuclear cooling towers?", "Defines double-branched open curve.", "Used in sonic boom shockwaves and towers."),
        ("Eccentricity of a Hyperbola", "e = sqrt(1 + b^2 / a^2)  (e > 1)", "Apollonius (200 BC)", "space", "beat_pulse", "space_tech", "How do spaceships escape Earth gravity into deep space?", "Characterizes unbound escape trajectories.", "Used in NASA gravity assist flybys."),
        ("Asymptotes of a Hyperbola", "y = +- (b / a) * x", "Apollonius (200 BC)", "abstract", "glitch_pop", "space_tech", "What straight lines bound hyperbolic paths at infinity?", "Defines limiting linear trajectories.", "Used in long-range radar navigation LORAN."),
        ("Rectangular Hyperbola Equation", "x * y = c^2", "Apollonius & Boyle (1662)", "nature", "ken_burns", "nature_history_lofi", "What curve connects pressure and volume in gas thermodynamics?", "Symmetric hyperbola with perp asymptotes.", "Used in thermodynamics Boyle's law."),
        ("Tangent to Parabola in Point Form", "y * y1 = 2*a*(x + x1)", "Descartes (1637)", "space", "beat_pulse", "space_tech", "How to calculate the exact reflection angle on a solar mirror?", "Finds tangent slope at any point.", "Used in laser reflection optics.")
    ]),
    (16, "Grade 11", [
        ("Trigonometric Limit Identity", "lim(x->0) [sin(x) / x] = 1", "Euler & Maclaurin (1742)", "abstract", "beat_pulse", "space_tech", "Why does sin x over x equal one when x approaches zero?", "Fundamental foundation of calculus derivatives.", "Used in signal sinc functions and DSP."),
        ("Exponential Limit Identity", "lim(x->0) [(e^x - 1) / x] = 1", "Euler (1748)", "space", "glitch_pop", "space_tech", "Why is e the only base that is its own instantaneous rate of change?", "Defines natural exponential slope.", "Used in population growth and physics."),
        ("Logarithmic Limit Identity", "lim(x->0) [ln(1 + x) / x] = 1", "Euler (1748)", "nature", "ken_burns", "nature_history_lofi", "How to calculate continuous compound interest growth?", "Calculates natural log derivative.", "Used in financial continuous models."),
        ("Definition of Derivative (First Principles)", "f'(x) = lim(h->0) [(f(x+h) - f(x)) / h]", "Newton & Leibniz (1684)", "space", "beat_pulse", "space_tech", "What is the single greatest formula in the history of science?", "Calculates instantaneous rate of change.", "Used in physics, AI gradients, and engineering."),
        ("Squeeze (Sandwich) Theorem", "If g(x) <= f(x) <= h(x) and limits match, lim f(x) = L", "Archimedes & Gauss (1800)", "abstract", "glitch_pop", "space_tech", "How to find limits of impossible oscillating functions?", "Traps functions between known bounds.", "Used in quantum convergence proofs."),
        ("Intermediate Value Theorem", "If f continuous on [a,b], it takes every value between f(a) & f(b)", "Bolzano (1817)", "nature", "ken_burns", "nature_history_lofi", "Why must there always be two opposite spots on Earth with equal temp?", "Guarantees root existence in continuous systems.", "Used in numerical bisection solvers."),
        ("Continuity Condition at a Point", "lim(x->a) f(x) = f(a)", "Cauchy (1821)", "space", "beat_pulse", "space_tech", "What mathematical rule prevents teleportation in physics?", "Ensures smooth unbroken function curves.", "Used in structural mechanics and fluid flow."),
        ("Derivative of Sine Function", "d/dx [sin(x)] = cos(x)", "Newton & Leibniz (1684)", "abstract", "glitch_pop", "space_tech", "Why is the rate of change of a wave shifted by 90 degrees?", "Differentiates harmonic waves.", "Used in electromagnetic wave physics."),
        ("Derivative of Exponential Function", "d/dx [e^x] = e^x", "Euler (1748)", "nature", "ken_burns", "nature_history_lofi", "What function is completely unchanged by differentiation?", "Models pure self-replicating growth.", "Used in nuclear reactions and biology."),
        ("Derivative of Natural Logarithm", "d/dx [ln(x)] = 1 / x", "Leibniz (1684)", "space", "beat_pulse", "space_tech", "Why is the rate of change of natural log equal to 1 over x?", "Connects logarithmic growth to inverse fractions.", "Used in information entropy and thermodynamics.")
    ]),
    (17, "Grade 12", [
        ("Derivative Power Rule", "d/dx [x^n] = n * x^(n - 1)", "Isaac Newton & Leibniz (1684)", "abstract", "beat_pulse", "space_tech", "How to differentiate any polynomial in one second?", "Multiplies by power and decrements exponent.", "Used in AI machine learning gradients."),
        ("Product Rule of Differentiation", "d/dx [u * v] = u' * v + u * v'", "Gottfried Wilhelm Leibniz (1684)", "space", "glitch_pop", "space_tech", "Why can't you just multiply two derivatives together?", "Differentiates products of changing variables.", "Used in kinetic energy and power formulas."),
        ("Quotient Rule of Differentiation", "d/dx [u / v] = (u'*v - u*v') / v^2", "Leibniz (1684)", "nature", "ken_burns", "nature_history_lofi", "How to calculate rate of change of ratios and fractions?", "Differentiates division of functions.", "Used in economic elasticity and physics."),
        ("Chain Rule of Differentiation", "dy/dx = (dy/du) * (du/dx)", "Leibniz (1676)", "space", "beat_pulse", "space_tech", "What calculus rule powers deep neural network backpropagation?", "Differentiates nested composite functions.", "Used in deep learning neural networks."),
        ("L'Hopital's Rule for 0/0 Indeterminates", "lim [f(x)/g(x)] = lim [f'(x)/g'(x)]", "Guillaume de l'Hôpital & Bernoulli (1696)", "abstract", "glitch_pop", "space_tech", "How to divide zero by zero and get a real number?", "Resolves 0/0 and inf/inf limits via slopes.", "Used in physics wave boundary limits."),
        ("Mean Value Theorem (MVT)", "f'(c) = (f(b) - f(a)) / (b - a)", "Joseph-Louis Lagrange (1797)", "nature", "ken_burns", "nature_history_lofi", "How can speed cameras prove you sped without seeing you speed?", "Guarantees instantaneous speed equals average speed.", "Used in highway average speed traps."),
        ("Rolle's Theorem", "If f(a)=f(b), then exists c where f'(c) = 0", "Michel Rolle (1691)", "space", "beat_pulse", "space_tech", "Why must a thrown ball reach a stationary peak before falling?", "Guarantees a stationary turning point.", "Used in optimization and root finding."),
        ("Second Derivative Test for Maxima/Minima", "If f'(c)=0 & f''(c)<0 => Maxima, f''(c)>0 => Minima", "Newton (1687)", "abstract", "glitch_pop", "space_tech", "How do companies find the exact price that maximizes profit?", "Determines curve curvature and peaks.", "Used in corporate revenue optimization."),
        ("Implicit Differentiation Formula", "d/dx [f(x, y)] = 0  => dy/dx = -Fx / Fy", "Leibniz (1684)", "nature", "ken_burns", "nature_history_lofi", "How to find slope of complex interwoven curves like circles?", "Differentiates without isolating y explicitly.", "Used in economics utility indifference curves."),
        ("Logarithmic Differentiation", "dy/dx = y * d/dx [ln(y)]", "Johann Bernoulli (1697)", "space", "beat_pulse", "space_tech", "How to differentiate functions raised to variable powers?", "Simplifies complex exponents via natural logs.", "Used in entropy derivative calculations.")
    ]),
    (18, "Grade 12", [
        ("Indefinite Integral Definition", "integral f(x) dx = F(x) + C", "Newton & Leibniz (1684)", "abstract", "beat_pulse", "space_tech", "What is the reverse operation of finding a derivative?", "Accumulates continuous changing quantities.", "Used in calculating total energy from power."),
        ("Power Rule of Integration", "integral x^n dx = (x^(n+1))/(n+1) + C  (n!=-1)", "Cavalieri & Newton (1635)", "space", "glitch_pop", "space_tech", "How to find total area under any polynomial curve?", "Reverses power rule differentiation.", "Used in physics work and displacement."),
        ("Integration of 1/x to Natural Log", "integral (1/x) dx = ln|x| + C", "Alphonse Antonio de Sarasa (1649)", "nature", "ken_burns", "nature_history_lofi", "Why does 1/x integrate to natural log instead of a polynomial?", "Fills the single gap in the integration power rule.", "Used in thermodynamics gas expansion work."),
        ("Integration of Exponential Function", "integral e^(ax) dx = (1/a) * e^(ax) + C", "Euler (1748)", "space", "beat_pulse", "space_tech", "How to integrate continuous compounding growth?", "Preserves exponential base scaled by constant.", "Used in electrical capacitor charging curves."),
        ("Integration by Substitution (u-sub)", "integral f(g(x))g'(x)dx = integral f(u)du", "Leibniz (1684)", "abstract", "glitch_pop", "space_tech", "What is the reverse of the calculus chain rule?", "Transforms complex integrals into simple variables.", "Used in fluid mechanics flow integrals."),
        ("Integration by Parts Formula", "integral u dv = u*v - integral v du", "Brook Taylor & Johann Bernoulli (1715)", "nature", "ken_burns", "nature_history_lofi", "How do physicists integrate products of polynomials and waves?", "Integrates product of two different functions.", "Used in Fourier analysis and quantum physics."),
        ("Integration of Sine Function", "integral sin(ax) dx = -(1/a)*cos(ax) + C", "Newton & Leibniz (1684)", "space", "beat_pulse", "space_tech", "What is the continuous accumulation of harmonic sine waves?", "Integrates oscillatory harmonic signals.", "Used in AC electrical energy transfer."),
        ("Integration of Cosine Function", "integral cos(ax) dx = (1/a)*sin(ax) + C", "Newton & Leibniz (1684)", "abstract", "glitch_pop", "space_tech", "How do sound engineers compute acoustic sound energy?", "Integrates cosine sound pressures.", "Used in acoustics and speaker design."),
        ("Standard Arctangent Integral", "integral 1/(x^2 + a^2) dx = (1/a)*arctan(x/a) + C", "Euler (1748)", "nature", "ken_burns", "nature_history_lofi", "How do rational polynomial fractions produce angles?", "Connects rational functions to inverse trig angles.", "Used in electrical impedance filtering."),
        ("Partial Fractions Integration", "P(x)/((x-a)(x-b)) = A/(x-a) + B/(x-b)", "Euler & Leibniz (1702)", "space", "beat_pulse", "space_tech", "How to break impossible fraction integrals into simple pieces?", "Decomposes complex rational fractions.", "Used in control systems transfer functions.")
    ]),
    (19, "Grade 12", [
        ("Fundamental Theorem of Calculus", "integral_a^b f(x)dx = F(b) - F(a)", "Newton & Leibniz (1684)", "abstract", "beat_pulse", "space_tech", "What is the master bridge connecting derivatives to areas?", "Calculates exact definite accumulated area.", "Used in all engineering, physics, and economics."),
        ("Area Under a Curve", "Area = integral_a^b y dx", "Newton (1684)", "space", "glitch_pop", "space_tech", "How do engineers calculate the structural load on bridge arches?", "Measures 2D area under arbitrary curves.", "Used in civil bridge load analysis."),
        ("Even Function Definite Integral Property", "integral_-a^a f(x)dx = 2 * integral_0^a f(x)dx", "Euler (1748)", "nature", "ken_burns", "nature_history_lofi", "How to cut complex definite integral calculations in half?", "Exploits mirror symmetry across y-axis.", "Used in digital signal spectrum analysis."),
        ("Odd Function Definite Integral Property", "integral_-a^a f(x)dx = 0", "Euler (1748)", "space", "beat_pulse", "space_tech", "Why do symmetric odd functions integrate to ZERO instantly?", "Positive and negative lobes cancel perfectly.", "Used in quantum wave parity calculations."),
        ("King's Property of Definite Integrals", "integral_a^b f(x)dx = integral_a^b f(a + b - x)dx", "Ancient & Modern Calculus Solvers", "abstract", "glitch_pop", "space_tech", "What is the legendary shortcut to solve impossible Olympiad integrals?", "Flips integral bounds without changing area.", "Used in competitive math and signal inversion."),
        ("Volume of Revolution (Disk Method)", "V = pi * integral_a^b [f(x)]^2 dx", "Bonaventura Cavalieri (1635)", "nature", "ken_burns", "nature_history_lofi", "How to calculate the exact volume of a 3D wine bottle or rocket fuselage?", "Rotates 2D curve around axis into 3D volume.", "Used in jet turbine manufacturing."),
        ("Arc Length of a Smooth Curve", "L = integral_a^b sqrt(1 + (f'(x))^2) dx", "Leibniz (1684)", "space", "beat_pulse", "space_tech", "How do roller coaster designers measure true track length in 3D?", "Integrates infinitesimal hypotenuse slices.", "Used in roller coaster design and road construction."),
        ("Surface Area of Solid of Revolution", "S = 2*pi * integral y * sqrt(1 + (y')^2) dx", "Archimedes & Leibniz (1684)", "abstract", "glitch_pop", "space_tech", "How much heat shield material covers an Apollo space capsule?", "Calculates 3D curved shell area.", "Used in spacecraft atmospheric heat shields."),
        ("Mean Value Theorem for Integrals", "f(c) = (1 / (b - a)) * integral_a^b f(x)dx", "Augustin-Louis Cauchy (1821)", "nature", "ken_burns", "nature_history_lofi", "What is the true continuous average value of a dynamic voltage?", "Finds average height of continuous curves.", "Used in root-mean-square RMS electrical voltage."),
        ("Trapezoidal Rule of Numerical Integration", "integral f(x)dx approx (h/2)*[y0 + 2(y1+...+yn-1) + yn]", "Newton (1676)", "space", "beat_pulse", "space_tech", "How do computers calculate integrals of raw sensor data?", "Approximates area using trapezoids.", "Used in flight recorder sensor integrations.")
    ]),
    (20, "Grade 12", [
        ("Vector Magnitude in 3D Space", "|v| = sqrt(x^2 + y^2 + z^2)", "Josiah Willard Gibbs & Heaviside (1881)", "abstract", "beat_pulse", "space_tech", "How does a drone calculate its true 3D spatial velocity vector?", "Calculates 3D Euclidean vector length.", "Used in drone flight controllers and 3D games."),
        ("Unit Vector Normalization", "u_hat = v / |v|", "William Rowan Hamilton (1843)", "space", "glitch_pop", "space_tech", "How do 3D game engines extract pure direction without changing speed?", "Scales any vector to unit length of 1.", "Used in video game character movement."),
        ("Vector Dot Product", "a . b = |a|*|b|*cos(theta) = ax*bx + ay*by + az*bz", "Gibbs (1881)", "nature", "ken_burns", "nature_history_lofi", "How do 3D graphics engines calculate sunlight reflection on characters?", "Measures alignment of two vectors.", "Used in 3D game lighting and AI embeddings."),
        ("Condition of Orthogonality (Perpendicular Vectors)", "a . b = 0", "Gibbs (1881)", "space", "beat_pulse", "space_tech", "How to verify if two spatial lines meet at a perfect 90 degree angle?", "Tests perpendicularity in any dimension.", "Used in orthogonal radar polarizations."),
        ("Vector Cross Product", "a x b = |a|*|b|*sin(theta) * n_hat", "Gibbs (1881)", "abstract", "glitch_pop", "space_tech", "How do mechanics calculate torque wrench twisting power?", "Produces perpendicular vector proportional to area.", "Used in torque, magnetic force, and robotics."),
        ("Condition of Collinearity for Vectors", "a x b = 0", "Gibbs (1881)", "nature", "ken_burns", "nature_history_lofi", "How do autopilot systems ensure an aircraft stays parallel to the runway?", "Tests parallel orientation.", "Used in aircraft instrument landing systems."),
        ("Scalar Triple Product (Box Product)", "[a b c] = a . (b x c)", "Gibbs (1881)", "space", "beat_pulse", "space_tech", "How to find the exact 3D volume of a skewed crystalline box?", "Calculates volume of parallelepiped.", "Used in crystallography and structural analysis."),
        ("Vector Equation of a Line in 3D", "r = a + lambda * b", "Descartes & Hamilton (1843)", "abstract", "glitch_pop", "space_tech", "How do laser scanning theodolites define infinite sight lines in space?", "Defines 3D line via point and direction.", "Used in 3D lidar laser surveying."),
        ("Equation of a Plane in Normal Form", "r . n_hat = d", "Descartes (1637)", "nature", "ken_burns", "nature_history_lofi", "How do computer graphics engines render flat walls and surfaces in 3D?", "Defines 2D plane in 3D space.", "Used in 3D game clipping planes."),
        ("Shortest Distance Between Skew Lines", "d = |(a2 - a1) . (b1 x b2)| / |b1 x b2|", "Hamilton (1843)", "space", "beat_pulse", "space_tech", "How do air traffic controllers ensure non-intersecting flight paths never collide?", "Calculates minimum distance between non-parallel 3D lines.", "Used in aircraft collision avoidance TCAS.")
    ]),
    (21, "Grade 12", [
        ("Separable Differential Equation Form", "dy / g(y) = f(x) dx", "Gottfried Leibniz (1691)", "abstract", "beat_pulse", "space_tech", "How to solve differential equations by separating variables?", "Splits equations into pure x and y integrals.", "Used in chemical reaction kinetics."),
        ("First Order Linear Differential Equation", "dy/dx + P(x)*y = Q(x)", "Leibniz & Johann Bernoulli (1692)", "space", "glitch_pop", "space_tech", "What equation governs electrical circuits and cooling objects?", "Standard 1st order dynamic system form.", "Used in RL and RC electrical circuits."),
        ("Integrating Factor Formula", "IF = e^(integral P(x) dx)", "Euler (1740)", "nature", "ken_burns", "nature_history_lofi", "What magic multiplier turns messy differential equations into pure derivatives?", "Converts linear ODEs into exact derivatives.", "Used in electrical circuit voltage analysis."),
        ("General Solution of Linear ODE", "y * IF = integral (Q(x) * IF) dx + C", "Euler (1740)", "space", "beat_pulse", "space_tech", "How to solve for system state across continuous time?", "Solves linear dynamical systems.", "Used in avionics autopilot feedback systems."),
        ("Newton's Law of Cooling", "dT/dt = -k * (T - T_ambient)", "Sir Isaac Newton (1701)", "abstract", "glitch_pop", "space_tech", "How do forensic detectives determine the exact time of death?", "Models heat transfer to surroundings.", "Used in forensic science and coffee cup cooling."),
        ("Exponential Population Growth Equation", "dN/dt = r * N  => N(t) = N0 * e^(rt)", "Thomas Malthus (1798)", "nature", "ken_burns", "nature_history_lofi", "How fast does an unconstrained bacterial colony or epidemic grow?", "Models uninhibited biological growth.", "Used in epidemiology virus spread models."),
        ("Radioactive Decay Law", "N(t) = N0 * e^(-lambda * t)", "Rutherford & Soddy (1902)", "space", "beat_pulse", "space_tech", "How do archaeologists date ancient Egyptian pharaoh tombs?", "Calculates atomic decay over time.", "Used in Carbon-14 archaeological dating."),
        ("Half-Life Decay Relationship", "T_half = ln(2) / lambda", "Ernest Rutherford (1904)", "abstract", "glitch_pop", "space_tech", "How to calculate the safety lifetime of nuclear reactor waste?", "Relates decay rate to half-life duration.", "Used in nuclear medicine dosage and safety."),
        ("Second Order Homogeneous ODE with Constant Coeffs", "a*y'' + b*y' + c*y = 0", "Euler (1743)", "nature", "ken_burns", "nature_history_lofi", "What equation governs car suspension springs and guitar strings?", "Models harmonic damping and oscillations.", "Used in vehicle shock absorbers and acoustics."),
        ("Simple Harmonic Motion Differential Equation", "d^2x/dt^2 + omega^2 * x = 0", "Hooke & Newton (1687)", "space", "beat_pulse", "space_tech", "What equation governs pendulum clocks, quartz watches, and sound waves?", "Defines pure frictionless harmonic oscillation.", "Used in quartz clocks and quantum oscillators.")
    ]),
    (22, "Grade 12", [
        ("Conditional Probability Definition", "P(A|B) = P(A and B) / P(B)", "Thomas Bayes & Kolmogorov (1933)", "abstract", "beat_pulse", "space_tech", "How do medical test diagnostics adjust when a patient tests positive?", "Calculates probability given prior evidence.", "Used in spam filters and medical testing."),
        ("Multiplication Rule of Probability", "P(A and B) = P(A) * P(B|A)", "Abraham de Moivre (1718)", "space", "glitch_pop", "space_tech", "How to calculate the probability of two dependent events occurring together?", "Connects joint probability to conditional rates.", "Used in financial default contagion models."),
        ("Law of Total Probability", "P(B) = sum(P(B|Ai) * P(Ai))", "Pierre-Simon Laplace (1812)", "nature", "ken_burns", "nature_history_lofi", "How do insurance companies calculate overall national crash risk?", "Sums probabilities across partitioned causes.", "Used in insurance risk underwriting."),
        ("Bayes' Theorem", "P(A|B) = [P(B|A) * P(A)] / P(B)", "Reverend Thomas Bayes (1763)", "space", "beat_pulse", "space_tech", "What equation updates belief with new evidence in artificial intelligence?", "Fundamental theorem of statistical inference.", "Used in AI machine learning, spam filters, and robotics."),
        ("Binomial Probability Distribution PMF", "P(X=k) = nCk * p^k * (1-p)^(n-k)", "Jacob Bernoulli (1713)", "abstract", "glitch_pop", "space_tech", "What are the exact odds of flipping exactly 7 heads out of 10 coin tosses?", "Calculates probability of k successes in n trials.", "Used in pharmaceutical drug clinical trials."),
        ("Mean of Binomial Distribution", "E[X] = n * p", "Bernoulli (1713)", "nature", "ken_burns", "nature_history_lofi", "If a basketball player hits 80% of shots, how many will they make in 50 tries?", "Calculates expected value of binomial trials.", "Used in manufacturing defect expectations."),
        ("Variance of Binomial Distribution", "Var(X) = n * p * (1 - p)", "Bernoulli (1713)", "space", "beat_pulse", "space_tech", "How to measure the uncertainty spread in coin flips and elections?", "Quantifies statistical dispersion.", "Used in political election polling errors."),
        ("Poisson Probability Distribution", "P(X=k) = (lambda^k * e^(-lambda)) / k!", "Siméon Denis Poisson (1837)", "abstract", "glitch_pop", "space_tech", "How do call centers predict customer phone call arrival traffic?", "Models rare events occurring in continuous time.", "Used in telecom traffic and radioactive counts."),
        ("Gaussian (Normal) Distribution PDF", "f(x) = [1/(sigma*sqrt(2pi))] * e^(-(x-mu)^2 / (2sigma^2))", "Carl Friedrich Gauss (1809)", "nature", "ken_burns", "nature_history_lofi", "What is the famous bell curve that governs human heights and IQs?", "Standard universal continuous distribution.", "Used in AI neural nets, finance, and quality control."),
        ("Expected Value of Discrete Random Variable", "E[X] = sum(x_i * P(x_i))", "Christiaan Huygens (1657)", "space", "beat_pulse", "space_tech", "How do casinos mathematically guarantee they always win in the long run?", "Calculates long-term weighted average outcome.", "Used in financial investment risk and game theory.")
    ]),
    (23, "B.Tech Engineering", [
        ("Matrix Multiplication Definition", "C_ij = sum(A_ik * B_kj)", "Arthur Cayley (1858)", "abstract", "beat_pulse", "space_tech", "What single matrix operation powers all modern 3D graphics and AI training?", "Combines linear transformations.", "Used in GPU shaders and Large Language Models."),
        ("Determinant of a 2x2 Matrix", "det(A) = a*d - b*c", "Cauchy & Cayley (1841)", "space", "glitch_pop", "space_tech", "How does a matrix scale 2D area during geometric transformation?", "Measures volume scaling factor.", "Used in computer graphics scaling."),
        ("Inverse of a Matrix", "A^(-1) = (1 / det(A)) * adj(A)", "Arthur Cayley (1858)", "nature", "ken_burns", "nature_history_lofi", "How do engineers reverse complex sensor transformations?", "Reverses linear matrix systems.", "Used in robot kinematics and cryptography."),
        ("Eigenvalue Characteristic Equation", "det(A - lambda * I) = 0", "Euler & Cauchy (1829)", "space", "beat_pulse", "space_tech", "How do civil engineers prevent bridges from collapsing in wind storms?", "Finds natural resonance frequencies.", "Used in structural vibrational resonance."),
        ("Eigenvector Definition", "A * v = lambda * v", "Euler, Lagrange & Cauchy (1829)", "abstract", "glitch_pop", "space_tech", "What special directions in space never rotate when transformed?", "Identifies invariant directional axes.", "Used in Google PageRank and facial recognition."),
        ("Cayley-Hamilton Theorem", "p(A) = 0", "Arthur Cayley & Hamilton (1858)", "nature", "ken_burns", "nature_history_lofi", "Why does every square matrix satisfy its own characteristic equation?", "Allows computing giant matrix powers rapidly.", "Used in aerospace control systems."),
        ("Orthogonal Matrix Property", "A^T * A = I  => A^(-1) = A^T", "Cauchy (1841)", "space", "beat_pulse", "space_tech", "How do 3D rotation engines rotate objects without distorting their shape?", "Preserves vector lengths and angles.", "Used in 3D gaming rotations and VR headsets."),
        ("Matrix Rank and Nullity Theorem", "Rank(A) + Nullity(A) = Number of Columns", "Sylvester (1884)", "abstract", "glitch_pop", "space_tech", "What fundamental theorem balances dimensions in linear systems?", "Connects image space to kernel nullspace.", "Used in data compression and network flow."),
        ("Matrix Diagonalization", "A = P * D * P^(-1)", "Cauchy (1829)", "nature", "ken_burns", "nature_history_lofi", "How to raise a 1000x1000 matrix to the millionth power in one second?", "Decomposes matrices into pure scaling diagonal form.", "Used in quantum simulation algorithms."),
        ("Trace of a Matrix", "Tr(A) = sum(A_ii) = sum(lambda_i)", "Cayley (1858)", "space", "beat_pulse", "space_tech", "Why does the sum of diagonal elements equal the sum of all eigenvalues?", "Invariant sum under coordinate transformations.", "Used in quantum density matrix mechanics.")
    ]),
    (24, "B.Tech Engineering", [
        ("Partial Derivative Definition", "df/dx = lim(h->0) [(f(x+h, y) - f(x, y)) / h]", "Euler & d'Alembert (1743)", "abstract", "beat_pulse", "space_tech", "How do climate models change temperature while holding pressure constant?", "Measures rate of change along one specific axis.", "Used in thermodynamics and AI gradients."),
        ("Gradient Vector in 3D", "grad(f) = (df/dx) i + (df/dy) j + (df/dz) k", "Hamilton & Gibbs (1881)", "space", "glitch_pop", "space_tech", "What vector points in the direction of steepest possible ascent?", "Defines multidimensional slope vector.", "Used in AI Gradient Descent optimization."),
        ("Directional Derivative", "D_u f = grad(f) . u_hat", "Cauchy (1827)", "nature", "ken_burns", "nature_history_lofi", "How steep is a mountain slope if you hike in an arbitrary compass heading?", "Calculates rate of change along unit direction.", "Used in aircraft terrain navigation."),
        ("Divergence of a Vector Field", "div(F) = dFx/dx + dFy/dy + dFz/dz", "Gibbs & Heaviside (1881)", "space", "beat_pulse", "space_tech", "How to measure whether a point in space is a net source or sink of fluid?", "Quantifies outward flux density.", "Used in Maxwell's electromagnetism and hydraulics."),
        ("Curl of a Vector Field", "curl(F) = det([i j k; d/dx d/dy d/dz; Fx Fy Fz])", "Gibbs (1881)", "abstract", "glitch_pop", "space_tech", "How do meteorologists measure the rotational spinning power of a tornado?", "Measures microscopic rotation of fields.", "Used in tornado aerodynamics and magnetic fields."),
        ("Laplacian Operator", "nabla^2 f = d^2f/dx^2 + d^2f/dy^2 + d^2f/dz^2", "Pierre-Simon Laplace (1799)", "nature", "ken_burns", "nature_history_lofi", "What master operator governs heat diffusion, waves, and electrostatic potentials?", "Measures difference between point and local average.", "Used in image sharpening and quantum wave mechanics."),
        ("Tangent Plane to 3D Surface", "Fx*(x - x0) + Fy*(y - y0) + Fz*(z - z0) = 0", "Monge (1795)", "space", "beat_pulse", "space_tech", "How do 3D CAD tools calculate surface tangents for aerodynamic cars?", "Constructs 2D tangent plane in 3D space.", "Used in car aerodynamic body design."),
        ("Jacobian Matrix Transformation", "J = det([dx/du dx/dv; dy/du dy/dv])", "Carl Gustav Jacobi (1841)", "abstract", "glitch_pop", "space_tech", "How do engineers change variables in multidimensional integrals?", "Scales area/volume under coordinate changes.", "Used in robotics forward kinematics."),
        ("Multivariable Taylor Series Expansion", "f(x+h, y+k) approx f + (h*fx + k*fy) + (1/2)(h^2*fxx + 2hk*fxy + k^2*fyy)", "Taylor & Euler (1755)", "nature", "ken_burns", "nature_history_lofi", "How do physics engines linearize complex non-linear aerodynamic forces?", "Approximates multivariable functions with polynomials.", "Used in nonlinear flight control systems."),
        ("Method of Lagrange Multipliers", "grad(f) = lambda * grad(g)", "Joseph-Louis Lagrange (1788)", "space", "beat_pulse", "space_tech", "How to find optimal design shapes under constrained budgets and materials?", "Solves constrained optimization problems.", "Used in economic portfolio optimization and AI.")
    ]),
    (25, "B.Tech Engineering", [
        ("Line Integral of a Vector Field", "W = integral_C F . dr", "Euler & Cauchy (1825)", "abstract", "beat_pulse", "space_tech", "How to calculate total mechanical work done moving along a curved path in gravity?", "Calculates work accumulated along curves.", "Used in gravitational work and magnetic loop fields."),
        ("Conservative Vector Field Condition", "curl(F) = 0  => F = grad(phi)", "Euler (1755)", "space", "glitch_pop", "space_tech", "Why is work done in a gravitational field independent of the path taken?", "Guarantees path independence in potential fields.", "Used in celestial gravitational orbital mechanics."),
        ("Surface Integral (Flux)", "Flux = double_integral_S F . n_hat dS", "Gauss (1813)", "nature", "ken_burns", "nature_history_lofi", "How to measure how much magnetic radiation penetrates a solar panel?", "Measures total vector flow through a 3D surface.", "Used in solar radiation and aerodynamics."),
        ("Green's Theorem in the Plane", "oint (L dx + M dy) = double_integral (dM/dx - dL/dy) dA", "George Green (1828)", "space", "beat_pulse", "space_tech", "How to calculate the area of an irregular island by walking only along its coastline?", "Connects 1D boundary line integral to 2D area.", "Used in planimeter area measuring tools."),
        ("Stokes' Theorem", "oint_C F . dr = double_integral_S (curl F) . n_hat dS", "George Gabriel Stokes (1854)", "abstract", "glitch_pop", "space_tech", "How does Faraday's law generate electricity from spinning magnets?", "Connects loop line integral to surface curl.", "Used in hydroelectric power turbine generators."),
        ("Gauss's Divergence Theorem", "double_integral_S F . n_hat dS = triple_integral_V (div F) dV", "Carl Friedrich Gauss (1813)", "nature", "ken_burns", "nature_history_lofi", "How to measure fluid exiting a pipe network by measuring only the internal sources?", "Connects boundary flux to internal volume divergence.", "Used in fluid dynamics and electrostatics."),
        ("Helmholtz Decomposition", "F = -grad(phi) + curl(A)", "Hermann von Helmholtz (1858)", "space", "beat_pulse", "space_tech", "Why can any vector field in the universe be split into pure stretch and pure spin?", "Splits fields into irrotational and solenoidal parts.", "Used in acoustic wave separation and geophysics."),
        ("Archimedes Principle via Divergence", "Buoyancy = - rho * g * Volume", "Archimedes & Gauss (1813)", "abstract", "glitch_pop", "space_tech", "How does vector calculus prove why giant steel aircraft carriers float on water?", "Integrates hydrostatic pressure over submerged hulls.", "Used in submarine ballast design."),
        ("Continuity Equation in Fluid Dynamics", "d(rho)/dt + div(rho * v) = 0", "Euler (1757)", "nature", "ken_burns", "nature_history_lofi", "What mathematical law ensures matter is never created or destroyed in fluid flow?", "Expresses conservation of mass in fluids.", "Used in pipeline gas transport and blood flow."),
        ("Maxwell's Flux Integral Form", "oint E . n_hat dS = Q_enclosed / epsilon_0", "Gauss & Maxwell (1861)", "space", "beat_pulse", "space_tech", "How does electric charge create electric field lines that radiate across space?", "Relates total electric flux to enclosed charge.", "Used in capacitor design and electrical shielding.")
    ]),
    (26, "B.Tech Engineering", [
        ("Laplace Transform Definition", "L{f(t)} = integral_0^inf e^(-st) * f(t) dt", "Pierre-Simon Laplace (1812)", "abstract", "beat_pulse", "space_tech", "How do engineers transform difficult differential equations into simple algebra?", "Converts time domain signals into frequency s-domain.", "Used in avionics flight control and audio filters."),
        ("First Shifting Theorem of Laplace", "L{e^(at) * f(t)} = F(s - a)", "Laplace (1812)", "space", "glitch_pop", "space_tech", "How does exponential damping shift system resonant frequencies?", "Shifts s-domain frequency by constant a.", "Used in damped vibration analysis."),
        ("Laplace Transform of Derivative", "L{f'(t)} = s * F(s) - f(0)", "Laplace (1812)", "nature", "ken_burns", "nature_history_lofi", "Why does Laplace turn calculus differentiation into simple multiplication by s?", "Replaces differential operators with algebraic powers.", "Used in solving electrical transient circuits."),
        ("Convolution Theorem of Laplace Transform", "L{f * g} = F(s) * G(s)", "Laplace & Borel (1899)", "space", "beat_pulse", "space_tech", "How to calculate the complete output of an audio amplifier given any input signal?", "Multiplies frequency responses directly.", "Used in audio reverb simulation and DSP."),
        ("Dirac Delta Function Property", "integral_-inf^inf delta(t - t0) * f(t) dt = f(t0)", "Paul Dirac (1927)", "abstract", "glitch_pop", "space_tech", "How do engineers model an instantaneous lightning strike or hammer blow?", "Models infinitely sharp instantaneous impulses.", "Used in earthquake shock testing and radar."),
        ("Heaviside Step Function", "u(t - a) = 1 if t >= a else 0", "Oliver Heaviside (1893)", "nature", "ken_burns", "nature_history_lofi", "How to model a light switch flipping on at exact time t equals a?", "Represents step switching events.", "Used in digital logic and circuit switching."),
        ("Fourier Series Expansion", "f(x) = a0/2 + sum(an*cos(nx) + bn*sin(nx))", "Joseph Fourier (1822)", "space", "beat_pulse", "space_tech", "Why can ANY sound or repeating signal be built from pure sine and cosine tones?", "Breaks periodic signals into harmonic frequencies.", "Used in music synthesizers and JPEG compression."),
        ("Continuous Fourier Transform", "F(omega) = integral_-inf^inf f(t) * e^(-i*omega*t) dt", "Fourier (1822)", "abstract", "glitch_pop", "space_tech", "How does Shazam recognize any song in two seconds from background noise?", "Converts continuous time signals to frequency spectra.", "Used in telecommunications, MRI, and Shazam."),
        ("Inverse Fourier Transform", "f(t) = (1/2pi) * integral_-inf^inf F(omega) * e^(i*omega*t) d(omega)", "Fourier (1822)", "nature", "ken_burns", "nature_history_lofi", "How to reconstruct an original audio waveform from its frequency spectrum?", "Rebuilds time waveforms from frequencies.", "Used in audio decompression and radio tuning."),
        ("Fast Fourier Transform Complexity", "FFT Complexity = O(N * log(N))", "Cooley & Tukey (1965)", "space", "beat_pulse", "space_tech", "What algorithmic breakthrough made digital telecommunications, MP3s, and Wi-Fi possible?", "Calculates discrete Fourier transforms ultra-fast.", "Used in Wi-Fi, 5G, MP3, and medical MRI scanners.")
    ]),
    (27, "B.Tech Engineering", [
        ("Newton-Raphson Method", "x_(n+1) = x_n - f(x_n) / f'(x_n)", "Sir Isaac Newton & Joseph Raphson (1690)", "abstract", "beat_pulse", "space_tech", "How do calculators compute square roots and solve complex equations to 20 decimal places?", "Iteratively converges to equation roots quadratically.", "Used in flight simulators and GPU shaders."),
        ("Bisection Numerical Method", "c = (a + b) / 2  (with bracket check)", "Bolzano (1817)", "space", "glitch_pop", "space_tech", "What bulletproof algorithm is guaranteed to find roots of continuous functions?", "Halves search interval at each step.", "Used in safety-critical aerospace solvers."),
        ("Runge-Kutta 4th Order Method (RK4)", "y_(n+1) = y_n + (h/6)*(k1 + 2k2 + 2k3 + k4)", "Carl Runge & Martin Kutta (1901)", "nature", "ken_burns", "nature_history_lofi", "How do NASA flight computers simulate spacecraft trajectories through orbital space?", "High-accuracy numerical integrator for differential equations.", "Used in rocket flight simulators and game physics."),
        ("Euler's Numerical Method for ODEs", "y_(n+1) = y_n + h * f(x_n, y_n)", "Leonhard Euler (1768)", "space", "beat_pulse", "space_tech", "What is the simplest fundamental algorithm for stepping forward in time in computer simulations?", "Steps forward linearly along tangent slopes.", "Used in basic video game physics engines."),
        ("Simpson's 1/3 Rule", "integral f(x)dx approx (h/3)*[y0 + 4*sum(y_odd) + 2*sum(y_even) + yn]", "Thomas Simpson (1743)", "abstract", "glitch_pop", "space_tech", "How do naval architects calculate the displacement volume of curved ship hulls?", "Approximates area using parabolic segments.", "Used in ship hull hydrodynamics."),
        ("Gauss-Seidel Iterative Method", "x_i^(k+1) = (1/A_ii)*[b_i - sum(A_ij*x_j^(k+1)) - sum(A_ij*x_j^k)]", "Gauss & Philipp von Seidel (1874)", "nature", "ken_burns", "nature_history_lofi", "How to solve massive systems of one million linear equations in heat transfer?", "Iteratively relaxes linear system components.", "Used in finite element structural analysis FEA."),
        ("Lagrange Interpolation Polynomial", "P(x) = sum(y_i * prod((x - x_j)/(x_i - x_j)))", "Joseph-Louis Lagrange (1795)", "space", "beat_pulse", "space_tech", "How to construct a smooth curve passing through any arbitrary set of data points?", "Constructs exact polynomial interpolation.", "Used in Shamir's secret sharing cryptography."),
        ("Gradient Descent Optimization Algorithm", "theta_(t+1) = theta_t - alpha * grad(J(theta))", "Augustin-Louis Cauchy (1847)", "abstract", "glitch_pop", "space_tech", "What optimization formula trains every artificial intelligence neural network on Earth?", "Steps parameters down the loss gradient slope.", "Used in ChatGPT, Tesla Autopilot, and AI neural nets."),
        ("Secant Root Finding Method", "x_(n+1) = x_n - f(x_n)*[(x_n - x_(n-1))/(f(x_n) - f(x_(n-1)))]", "Ancient & Modern Numerical Math", "nature", "ken_burns", "nature_history_lofi", "How to find roots rapidly when computing an analytical derivative is too hard?", "Approximates derivatives via secant lines.", "Used in financial option root finders."),
        ("Finite Difference Derivative Approximation", "f'(x) approx [f(x + h) - f(x - h)] / (2*h)", "Newton & Taylor (1715)", "space", "beat_pulse", "space_tech", "How do supercomputers compute derivatives from discrete weather grid cells?", "Central difference approximation with O(h^2) accuracy.", "Used in global weather forecasting supercomputers.")
    ]),
    (28, "B.Tech Higher Math", [
        ("Cauchy-Riemann Equations", "du/dx = dv/dy  and  du/dy = -dv/dx", "Augustin-Louis Cauchy & Riemann (1851)", "abstract", "beat_pulse", "space_tech", "What secret condition must a complex function satisfy to be truly differentiable?", "Ensures complex differentiability (analyticity).", "Used in 2D fluid aerodynamics and electrostatics."),
        ("Harmonic Conjugate Equation", "nabla^2 u = d^2u/dx^2 + d^2u/dy^2 = 0", "Laplace & Riemann (1851)", "space", "glitch_pop", "space_tech", "Why do airflow streamline contours always cross equipotential lines at 90 degrees?", "Guarantees orthogonal family curves.", "Used in airplane wing airflow modeling."),
        ("Cauchy's Integral Theorem", "oint_C f(z) dz = 0", "Cauchy (1825)", "nature", "ken_burns", "nature_history_lofi", "Why does looping any closed contour around an analytic function integrate to ZERO?", "Path independence in simply connected complex domains.", "Used in complex circuit analysis."),
        ("Cauchy's Integral Formula", "f(z0) = (1 / 2pi*i) * oint_C [f(z) / (z - z0)] dz", "Cauchy (1831)", "space", "beat_pulse", "space_tech", "How can the value of a function anywhere inside a region be known from its boundary alone?", "Calculates interior values from boundary contour.", "Used in boundary element engineering BEM."),
        ("Cauchy's Residue Theorem", "oint_C f(z) dz = 2*pi*i * sum(Residues)", "Cauchy (1831)", "abstract", "glitch_pop", "space_tech", "How do physicists evaluate impossible real integrals by walking through complex poles?", "Calculates complex contour integrals via pole residues.", "Used in quantum field theory and optics."),
        ("Residue at a Simple Pole", "Res(f, c) = lim(z->c) [(z - c) * f(z)]", "Cauchy (1831)", "nature", "ken_burns", "nature_history_lofi", "How to extract the residue strength of an isolated mathematical singularity?", "Extracts Laurent series minus-one coefficient.", "Used in electrical filter transfer poles."),
        ("Laurent Series Expansion", "f(z) = sum(a_n * (z - z0)^n, n=-inf..inf)", "Pierre Alphonse Laurent (1843)", "space", "beat_pulse", "space_tech", "What series expansion handles functions containing singularities and poles?", "Expands functions in positive and negative powers.", "Used in signal processing Z-transforms."),
        ("Conformal Mapping Property", "arg(w') is constant  => Preserves Angles", "Gauss & Riemann (1851)", "abstract", "glitch_pop", "space_tech", "How can you deform space while preserving every single intersection angle?", "Angle-preserving geometric coordinate transformation.", "Used in cartography map projections."),
        ("Joukowsky Aerodynamic Transformation", "w = z + c^2 / z", "Nikolai Zhukovsky (1906)", "nature", "ken_burns", "nature_history_lofi", "How did early aviation engineers calculate airplane wing lift from simple circle math?", "Transforms circles into aerodynamic airfoil shapes.", "Used in aircraft wing lift calculations."),
        ("Riemann Mapping Theorem", "Any simply connected open domain is conformally equivalent to unit disk", "Bernhard Riemann (1851)", "space", "beat_pulse", "space_tech", "Why can any smooth closed 2D shape in the universe be mapped to a circle?", "Establishes topological equivalence of 2D domains.", "Used in computer vision brain surface mapping.")
    ]),
    (29, "B.Tech Higher Math", [
        ("Markov Chain State Transition", "P(X_(n+1) = j | X_n = i) = P_ij", "Andrey Markov (1906)", "abstract", "beat_pulse", "space_tech", "How do autocomplete keyboards predict your next word based on current state?", "Models memoryless stochastic transitions.", "Used in smartphone keyboard prediction and Google search."),
        ("Stationary Distribution of Markov Chain", "pi * P = pi  (with sum(pi) = 1)", "Markov (1906)", "space", "glitch_pop", "space_tech", "Where do random web surfers eventually end up on the internet in the long run?", "Finds steady-state equilibrium probabilities.", "Used in Google PageRank algorithm."),
        ("Shannon Information Entropy", "H(X) = - sum(P(x) * log2(P(x)))", "Claude Shannon (Father of Information Theory, 1948)", "nature", "ken_burns", "nature_history_lofi", "What equation measures the fundamental information content and compressibility of data?", "Quantifies information uncertainty in bits.", "Used in ZIP file compression, Wi-Fi, and 5G."),
        ("Ordinary Least Squares Matrix Formula", "beta = (X^T * X)^(-1) * X^T * y", "Gauss & Legendre (1805)", "space", "beat_pulse", "space_tech", "What closed-form matrix formula fits optimal trendlines through massive data clouds?", "Finds optimal linear regression weights.", "Used in econometric forecasting and AI."),
        ("Singular Value Decomposition (SVD)", "A = U * Sigma * V^T", "Eugenio Beltrami & Camille Jordan (1873)", "abstract", "glitch_pop", "space_tech", "How do Netflix and Spotify recommend movies and songs by factorizing user ratings?", "Decomposes any matrix into rank components.", "Used in Netflix recommendation systems and image compression."),
        ("Principal Component Analysis (PCA)", "Covariance Matrix: C = (1/N) * X^T * X", "Karl Pearson (1901)", "nature", "ken_burns", "nature_history_lofi", "How to compress 1000 data dimensions into 2 visible dimensions without losing signal?", "Finds axes of maximum data variance.", "Used in facial recognition and genomics."),
        ("Logistic Sigmoid Function", "sigma(z) = 1 / (1 + e^(-z))", "Pierre François Verhulst (1838)", "space", "beat_pulse", "space_tech", "How do AI neural networks squash infinite linear numbers into clean 0 to 1 probabilities?", "Nonlinear activation function for binary classification.", "Used in AI logistic regression and neural nets."),
        ("Softmax Multiclass Probability Function", "Softmax(z_i) = e^(z_i) / sum(e^(z_j))", "Ludwig Boltzmann & Gibbs (1868)", "abstract", "glitch_pop", "space_tech", "How do Large Language Models like ChatGPT pick the next most likely token word?", "Converts raw logit scores into probability distributions.", "Used in ChatGPT, Claude, and LLM token selection."),
        ("Cross-Entropy Loss Function", "L = - sum(y_i * ln(y_hat_i))", "Shannon & Kullback (1951)", "nature", "ken_burns", "nature_history_lofi", "What loss equation penalizes AI neural networks when their predictions are wrong?", "Measures divergence between predicted and true distributions.", "Used in training all modern deep learning models."),
        ("Google PageRank Formula", "PR(u) = (1 - d)/N + d * sum(PR(v) / L(v))", "Larry Page & Sergey Brin (1998)", "space", "beat_pulse", "space_tech", "What single mathematical formula built Google into a trillion-dollar company?", "Ranks web pages by random walk link authority.", "Used in Google search engine web ranking.")
    ]),
    (30, "Grand Finale: Crown Equations", [
        ("Euler's Identity", "e^(i * pi) + 1 = 0", "Leonhard Euler (1748)", "abstract", "beat_pulse", "space_tech", "What is widely voted by mathematicians as the single most beautiful equation in human history?", "Unifies the 5 fundamental constants: 0, 1, e, i, and pi.", "Considered the pinnacle of mathematical beauty and complex analysis."),
        ("Einstein's Mass-Energy Equivalence", "E = m * c^2", "Albert Einstein (1905)", "space", "glitch_pop", "space_tech", "How can a single gram of matter power an entire city with energy?", "Proves mass is concentrated energy scaled by speed of light squared.", "Powers nuclear energy, solar fusion, and astrophysics."),
        ("Maxwell's Electromagnetic Equations", "curl(B) = mu0*J + mu0*eps0*(dE/dt)", "James Clerk Maxwell (1861)", "nature", "ken_burns", "nature_history_lofi", "What four equations unified electricity, magnetism, and light into one force?", "Unifies electromagnetism and predicted radio waves.", "Powers Wi-Fi, electric motors, power grids, and radar."),
        ("Schrodinger's Quantum Wave Equation", "i*hbar * (d/dt) psi = H_hat * psi", "Erwin Schrödinger (1926)", "space", "beat_pulse", "space_tech", "What equation governs the quantum probability wave of every subatomic electron?", "Defines quantum wave mechanics and atomic states.", "Powers microchip silicon transistors and quantum computing."),
        ("Einstein's Field Equations of General Relativity", "G_uv = (8*pi*G / c^4) * T_uv", "Albert Einstein (1915)", "abstract", "glitch_pop", "space_tech", "How does matter tell spacetime how to curve, and spacetime tell matter how to move?", "Defines gravity as the curvature of 4D spacetime.", "Powers GPS satellite orbital clock corrections and black hole physics."),
        ("Navier-Stokes Fluid Dynamics Equations", "rho*(dv/dt + v.grad(v)) = -grad(p) + mu*nabla^2(v) + f", "Claude-Louis Navier & George Stokes (1845)", "nature", "ken_burns", "nature_history_lofi", "What Millennium Prize equation governs ocean currents, tornadoes, and airplane lift?", "Models conservation of momentum in viscous fluids.", "Used in airplane aerodynamics, weather forecasts, and F1 racing."),
        ("Black-Scholes Financial Options Equation", "dV/dt + (1/2)*sigma^2*S^2*(d^2V/dS^2) + r*S*(dV/dS) - r*V = 0", "Fischer Black & Myron Scholes (1973)", "space", "beat_pulse", "space_tech", "What Nobel-prize winning equation founded modern multi-trillion dollar Wall Street derivatives trading?", "Calculates risk-neutral derivative option prices.", "Powers global stock options and hedge fund pricing engines."),
        ("RSA Cryptography Core Equation", "M^(e * d) = M (mod n)", "Rivest, Shamir & Adleman (1977)", "abstract", "glitch_pop", "space_tech", "What number theory equation secures every bank transaction, password, and credit card on Earth?", "Secures asymmetric public-key encryption via prime factorization.", "Powers HTTPS web security, online banking, and crypto wallets."),
        ("Boltzmann's Statistical Entropy Formula", "S = k_B * ln(W)", "Ludwig Boltzmann (1877)", "nature", "ken_burns", "nature_history_lofi", "Why does time only flow forward and never backward in our universe?", "Connects macroscopic entropy to microscopic microstates W.", "Defines the thermodynamic arrow of time and engine efficiency."),
        ("Dirac Relativistic Quantum Equation", "(i * gamma^mu * d_mu - m) * psi = 0", "Paul Dirac (1928)", "space", "beat_pulse", "space_tech", "What equation predicted the existence of antimatter before anyone had ever seen it?", "Unifies quantum mechanics with special relativity and electron spin.", "Predicted antimatter and founded modern particle physics.")
    ])
]

# Assemble the complete 300 database
for day_num, grade_lvl, eq_list in (RAW_CURRICULUM_DATA + DAYS_TOPICS):
    for offset, (name, form, founder, cat, motion, bgm, hook, purp, apps, *extra) in enumerate(eq_list, 1):
        g_num = (day_num - 1) * 10 + offset
        
        # Origin & cta formatting
        founder_orig = extra[0] if len(extra) > 0 else f"Discovered by {founder}."
        purpose_str = extra[1] if len(extra) > 1 else f"Its purpose is to: {purp}"
        apps_str = extra[2] if len(extra) > 2 else f"Real-world tech uses: {apps}"
        loop_cta = extra[3] if len(extra) > 3 else f"Master every law of mathematics! Like this video and subscribe to our channel for equation number {g_num+1}!"

        ALL_300_EQUATIONS.append({
            "day": day_num,
            "day_eq_num": offset,
            "global_eq_num": g_num,
            "grade_level": grade_lvl,
            "equation_name": name,
            "formula": form,
            "founder": founder,
            "category": cat,
            "motion_style": motion,
            "bgm_vibe": bgm,
            "hook": hook,
            "founder_origin": founder_orig,
            "purpose": purpose_str,
            "applications": apps_str,
            "loop_cta": loop_cta
        })

print(f"Total Equations Assembled: {len(ALL_300_EQUATIONS)}")

# Write to target python module
output_file = r"c:\Users\tsapa\Desktop\CODEX\master_30days_math_curriculum_300eq.py"

header = '''"""
MASTER 30-DAY MATHEMATICS SHORTS CURRICULUM: 300 EQUATIONS (10 EQUATIONS / DAY)
========================================================================================
From Grade 7 Fundamentals -> Grade 10 Algebra -> Intermediate 12th Calculus -> B.Tech Engineering.

PROGRESSION STRUCTURE:
  - Days 01-05 (Eqs 001-050): Middle School Fundamentals (Grades 7 & 8)
  - Days 06-12 (Eqs 051-120): High School Algebra, Geometry & Trigonometry (Grades 9 & 10)
  - Days 13-22 (Eqs 121-220): Intermediate / Senior Secondary Calculus & Vectors (Grades 11 & 12)
  - Days 23-30 (Eqs 221-300): B.Tech Engineering Mathematics & Crown Equations of Science

EVERY EQUATION FOLLOWS THE STRICT 5-POINT MODEL:
  1. What is the equation? (Formula HUD persistent from start to end)
  2. Who discovered it? (Founder & Year)
  3. What is its core purpose? (Intuitive breakdown)
  4. Real-world applications (Daily tech, engineering, AI, space, gaming, banking)
  5. Mind-blowing takeaway + Like and Subscribe CTA in the final 7 seconds
"""

'''

python_code = header + f"MASTER_30DAYS_MATH_EQUATIONS = {json.dumps(ALL_300_EQUATIONS, indent=4)}\n\n" + """
def get_math_equation_by_global_index(global_index: int) -> dict:
    \"\"\"Returns equation dictionary by 1-based global index (1-300).\"\"\"
    idx = (global_index - 1) % len(MASTER_30DAYS_MATH_EQUATIONS)
    return MASTER_30DAYS_MATH_EQUATIONS[idx]

def get_30day_math_batch(day: int) -> list:
    \"\"\"Returns all 10 equations for a specific day (1-30).\"\"\"
    start = (day - 1) * 10
    return MASTER_30DAYS_MATH_EQUATIONS[start:start+10]

def format_math_narration(eq: dict) -> str:
    \"\"\"Builds the full 60-second narration script for video generation.\"\"\"
    return f"{eq['hook']} {eq['founder_origin']} {eq['purpose']} {eq['applications']} {eq['loop_cta']}"

if __name__ == "__main__":
    print("=" * 80)
    print(f"  30-DAY MASTER MATHEMATICS CURRICULUM ({len(MASTER_30DAYS_MATH_EQUATIONS)} EQUATIONS / 10 PER DAY)")
    print("=" * 80)
    for day in range(1, 31):
        batch = get_30day_math_batch(day)
        print(f"\\n--- DAY {day:02d} ({batch[0]['grade_level']}) ---")
        for eq in batch:
            print(f"  [{eq['global_eq_num']:03d}] {eq['equation_name']:<42} | {eq['formula']:<32} | {eq['founder']}")
    print("\\n" + "=" * 80)
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(python_code)

print(f"Successfully generated {output_file} with {len(ALL_300_EQUATIONS)} equations.")

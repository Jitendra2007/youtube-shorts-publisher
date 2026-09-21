"""
CURIOSITY INFINITE SCRIPT MATRIX & GENERATOR (30+ HOURS CAPACITY)
====================================================================================
Generates endless, ultra-high retention 1-to-2 minute Shorts scripts designed
for maximum viewer watch time, psychological suspense, and seamless infinite replay loops.

RETENTION MECHANISMS:
1. The Open Information Gap: Promises an answer that is only revealed in the final 10 seconds.
2. The Mid-Script Escalation: "Wait, it gets crazier..." resets attention at second 30.
3. The Seamless Loop Outro: The final sentence flows directly back into the opening hook.
4. Integrated Call-To-Action: Encourages Likes & Subscriptions naturally within the mystery.
"""

import random

import random

# ── EXPANSIVE TOPIC DATABASE (HIGH-RETENTION CURIOSITY KERNELS) ─────────────
# Every script is designed with:
# 1. 0-3s Interrupt Hook
# 2. 7-20s Grounded Dilemma (Retention Anchor)
# 3. 20-42s Scientific / Historic Escalation ("Wait, it gets crazier...")
# 4. 42-54s Mind-Blowing Revelation / Twist
# 5. 54-75s+ Seamless Loop Outro & Integrated Like/Subscribe CTA

CURIOSITY_TOPIC_BANK = [
    # =========================================================================
    # 🧠 CATEGORY 1: MIND-BLOWING & PSYCHOLOGICAL FACTS
    # (Audio: Atmospheric Trap, Dark Tranquility, Ticking Clock, X-Files)
    # (Motion: Ken Burns Slow Pan & Zoom, Subtle Mystery Pulse)
    # =========================================================================
    {
        "id": "mind_doorway_effect",
        "category": "dark_moody",
        "motion_style": "ken_burns",
        "bgm_vibe": "psychology_mystery",
        "title": "The Doorway Effect: Why You Forget What You Came For 🚪",
        "youtube_title": "Why Walking Through A Door Erases Your Memory 🚪 #shorts #psychology #brain #mind",
        "tags": ["psychology", "brain", "doorwayeffect", "memory", "facts", "science", "shorts", "viral"],
        "scenery_keywords": ["dark", "shadow", "abstract"],
        "hook": "Have you ever walked into a room and completely forgotten why you went in there in the first place?",
        "dilemma": "You stand there staring into space feeling like an idiot. But neuroscientists at the University of Notre Dame discovered this is not a memory failure — it is a physical glitch in how your brain processes reality.",
        "science": "Your brain compartmentalizes your thoughts into mental event horizons. When you pass through a physical doorway, your hippocampus treats the new room as a brand new environment and automatically purges the working memory of the previous room to save cognitive RAM.",
        "twist": "Your mind literally wipes your short-term thoughts clean simply because you crossed a wooden threshold into another room. To get your memory back, walking back through the same door instantly reloads the deleted data from your brain's cache.",
        "loop_cta": "So next time you forget why you entered a room, remember that your environment controls your thoughts more than you do. Like this video and subscribe to our channel for daily brain-expanding secrets."
    },
    {
        "id": "mind_call_of_the_void",
        "category": "dark_moody",
        "motion_style": "ken_burns",
        "bgm_vibe": "psychology_mystery",
        "title": "The Call of the Void: The Sudden Urge to Jump 🧗",
        "youtube_title": "The Terrifying Urge To Jump: The Call of the Void 🧗 #shorts #psychology #mind #mystery",
        "tags": ["psychology", "callofthevoid", "brain", "neuroscience", "humanbody", "shorts", "viral"],
        "scenery_keywords": ["mountain", "cliff", "dark"],
        "hook": "Have you ever stood on the edge of a high cliff or balcony and felt a sudden, terrifying urge to jump?",
        "dilemma": "You are not suicidal and you have no desire to hurt yourself, yet for a split second, an eerie voice in your mind whispers: What if you just stepped off?",
        "science": "Psychologists call this The Call of the Void or L'appel du vide. In clinical studies, over fifty percent of mentally healthy humans experience this exact sensation. It happens because your subconscious survival reflexes process danger faster than your conscious mind.",
        "twist": "Your instinctual brain detects mortal danger and jerks you backward before your conscious brain understands why. When your conscious mind catches up a millisecond later, it misinterprets your physical jolt as a secret desire to jump. The thought is actually your brain's intense desire to keep you alive.",
        "loop_cta": "Your mind creates the fear of falling solely to ensure you survive. If this blew your mind, hit like and subscribe to our channel for more hidden human psychology."
    },
    {
        "id": "mind_baader_meinhof",
        "category": "abstract",
        "motion_style": "glitch_pop",
        "bgm_vibe": "psychology_mystery",
        "title": "The Baader-Meinhof Phenomenon: Reality Following You 👁️",
        "youtube_title": "Why A Word You Just Learned Suddenly Appears Everywhere 👁️ #shorts #psychology #brain",
        "tags": ["psychology", "baadermeinhof", "frequencyillusion", "brain", "facts", "shorts", "viral"],
        "scenery_keywords": ["abstract", "pattern", "neon"],
        "hook": "Have you ever learned a brand new word or noticed a specific car model, and suddenly you start seeing it everywhere you go?",
        "dilemma": "It feels like the universe is glitching or secretly placing clues around you. But cognitive scientists call this the Frequency Illusion or the Baader-Meinhof Phenomenon.",
        "science": "Every second, your sensory organs take in over eleven million bits of raw data, but your conscious brain can only process about fifty bits. When you learn something new, your brain's reticular activating system flags that information as important.",
        "twist": "The car or word was not missing before; your brain was simply deleting it from your conscious awareness to prevent sensory overload. The moment you pay attention, your mind allows you to see the hidden layer of reality that was always there.",
        "loop_cta": "How many other secrets around you is your brain currently hiding from your eyes? Like this video and subscribe to our channel for everyday mind-expanding revelations."
    },
    {
        "id": "mind_capgras_delusion",
        "category": "dark_moody",
        "motion_style": "ken_burns",
        "bgm_vibe": "psychology_mystery",
        "title": "The Capgras Delusion: When Loved Ones Become Impostors 👥",
        "youtube_title": "The Chilling Condition Where Your Family Becomes Impostors 👥 #shorts #psychology #mystery",
        "tags": ["psychology", "capgras", "brain", "neuroscience", "horror", "mind", "shorts", "viral"],
        "scenery_keywords": ["dark", "shadow", "gothic"],
        "hook": "What if you woke up tomorrow, looked at your mother or best friend, and became convinced they were an identical clone impostor?",
        "dilemma": "This is not a horror movie plot; it is a real neurological disorder known as the Capgras Delusion. Patients recognize their family member's exact face, voice, and memories, but remain unshakably convinced they are a synthetic imposter.",
        "science": "Normally, facial recognition in your temporal lobe sends an immediate emotional signal to your amygdala, giving you a warm feeling of familiarity. In Capgras patients, the facial recognition pathway works perfectly, but the emotional wire is severed.",
        "twist": "Because the patient sees their mother's face but feels absolute zero emotional connection, the logical brain invents a terrifying explanation: If this person looks like my mother but does not feel like her, they must be an impostor.",
        "loop_cta": "Your reality is entirely manufactured by emotional wires inside your skull. Make sure to like this video and subscribe to our channel for more deep neurological mysteries."
    },
    {
        "id": "mind_phantom_vibration",
        "category": "abstract",
        "motion_style": "glitch_pop",
        "bgm_vibe": "psychology_mystery",
        "title": "Phantom Vibration Syndrome: Your Phone Altering Your Nervous System 📱",
        "youtube_title": "Why You Feel Your Phone Vibrate When Nobody Called 📱 #shorts #psychology #tech #brain",
        "tags": ["psychology", "technology", "brain", "nervoussystem", "facts", "shorts", "viral"],
        "scenery_keywords": ["abstract", "neon", "dark"],
        "hook": "Have you ever felt your phone vibrate in your pocket, reached down to check it, only to realize nobody called or texted you?",
        "dilemma": "Over ninety percent of smartphone users experience this regularly. But this is not an equipment glitch — your nervous system has physically rewired itself.",
        "science": "Neurobiologists call this Phantom Vibration Syndrome. Because our brains anticipate social connection and notifications constantly, your cerebral cortex now treats clothing friction or slight muscle twitches as incoming digital signals.",
        "twist": "Your brain has literally incorporated your smartphone into your biological body schema, treating digital notifications with the exact same neurological urgency as physical touch on your skin.",
        "loop_cta": "How deeply has technology merged with your subconscious mind? Give this video a like and subscribe to our channel for daily psychological revelations."
    },
    {
        "id": "mind_hypnagogic_jerk",
        "category": "dark_moody",
        "motion_style": "beat_pulse",
        "bgm_vibe": "psychology_mystery",
        "title": "The Hypnic Jerk: Why You Fall When Falling Asleep 🛏️",
        "youtube_title": "Why Your Body Suddenly Jolts When You Fall Asleep 🛏️ #shorts #science #brain #body",
        "tags": ["sleep", "brain", "neuroscience", "hypnicjerk", "facts", "shorts", "viral"],
        "scenery_keywords": ["dark", "night", "shadow"],
        "hook": "Right as you drift off to sleep, do you ever feel like you are suddenly falling from the sky, causing your entire body to violently jerk awake?",
        "dilemma": "Your heart races and your adrenaline spikes out of nowhere. Evolutionary biologists discovered this violent twitch is actually an ancient survival reflex that kept our ancestors alive.",
        "science": "Known as a hypnic jerk or sleep start, it occurs as your motor system transitions into sleep paralysis. If your heart rate and muscle tension drop too rapidly, your subconscious brain misinterprets the rapid relaxation as physical death or falling out of a tree.",
        "twist": "To prevent you from dying, your brain fires a massive jolt of electrical energy through your spinal cord to kickstart your muscles back to life. That sudden shock is your brain testing if you are still alive.",
        "loop_cta": "Your ancient primal instincts are always awake, protecting you in the dark. Like this video and subscribe to our channel for more hidden truths of the human body."
    },

    # =========================================================================
    # 🚀 CATEGORY 2: COSMIC & FUTURISTIC TECH FACTS
    # (Audio: Space Ambient, Deep Cosmic Drone, Cyberpunk Synthwave, Transcendence)
    # (Motion: Ken Burns Deep Pan & Zoom, Cosmic Star Drift)
    # =========================================================================
    {
        "id": "space_false_vacuum_decay",
        "category": "space",
        "motion_style": "ken_burns",
        "bgm_vibe": "space_tech",
        "title": "False Vacuum Decay: The Instant Cosmic Eraser 🌌",
        "youtube_title": "The Terrifying Physics Event That Could Delete The Universe Instantly 🌌 #shorts #physics #space",
        "tags": ["space", "physics", "vacuumdecay", "universe", "higgsboson", "science", "shorts", "viral"],
        "scenery_keywords": ["space", "cosmos", "galaxy"],
        "hook": "What if the fundamental fabric of the universe could unravel at the speed of light with zero warning?",
        "dilemma": "In theoretical particle physics, there is a catastrophe scenario known as False Vacuum Decay. Everything in our universe, from atoms to light, is governed by quantum fields at their lowest energy state.",
        "science": "However, calculations from the Higgs boson indicate that our universe might not be in a true ground state, but rather a temporary false vacuum. If a single quantum fluctuation occurs anywhere in the cosmos, a bubble of true vacuum will form.",
        "twist": "This bubble would expand outward at the exact speed of light, destroying all chemical bonds, atoms, and physical laws in its path. Because it moves at the speed of light, you could never see it coming — our solar system would simply cease to exist in a zero-second flash.",
        "loop_cta": "The universe exists on a razor's edge of quantum stability. Like this video and subscribe to our channel for daily mind-bending journeys into cosmic physics."
    },
    {
        "id": "space_rogue_planets",
        "category": "space",
        "motion_style": "ken_burns",
        "bgm_vibe": "space_tech",
        "title": "Rogue Planets: The Dark Wanderers of The Galaxy 🪐",
        "youtube_title": "Billions of Giant Dark Planets Wandering The Cold Galaxy 🪐 #shorts #space #universe #facts",
        "tags": ["space", "rogueplanets", "astronomy", "universe", "cosmos", "science", "shorts", "viral"],
        "scenery_keywords": ["space", "stars", "planet"],
        "hook": "Did you know there are billions of giant planets in our galaxy that have no sun, drifting through pure eternal darkness?",
        "dilemma": "Known as rogue planets or nomad worlds, these celestial giants were violently ejected from their home solar systems billions of years ago by gravitational tugs from larger stars.",
        "science": "Astronomers estimate there are more rogue planets wandering the Milky Way than there are stars in the sky. With surface temperatures near absolute zero, their atmospheres have collapsed into frozen oceans of liquid methane and solid nitrogen.",
        "twist": "Yet deep beneath their frozen crusts, radioactive decay and geothermal vents could maintain warm liquid oceans where alien aquatic life may have evolved in pitch-black darkness for billions of years without ever knowing stars exist.",
        "loop_cta": "Could our solar system encounter one of these dark wanderers in the deep future? Hit like and subscribe to our channel for everyday cosmic truths."
    },
    {
        "id": "space_great_attractor",
        "category": "space",
        "motion_style": "ken_burns",
        "bgm_vibe": "space_tech",
        "title": "The Great Attractor: What Is Pulling Our Galaxy? 🧲",
        "youtube_title": "The Mysterious Force Pulling Our Entire Galaxy Across Space 🧲 #shorts #space #universe #mystery",
        "tags": ["space", "greatattractor", "universe", "astronomy", "physics", "mystery", "shorts", "viral"],
        "scenery_keywords": ["space", "galaxy", "cosmos"],
        "hook": "Right now, as you sit reading this, our entire Milky Way galaxy is being dragged across the cosmos at two million kilometers per hour.",
        "dilemma": "We are not drifting randomly. Our galaxy, along with millions of other surrounding galaxies across hundreds of millions of light-years, is being violently pulled toward a single point in space known as The Great Attractor.",
        "science": "Located over two hundred million light-years away in the direction of the Centaurus constellation, this point exerts the gravitational pull of tens of thousands of galaxies combined. What makes it terrifying is that it sits directly in the Zone of Avoidance.",
        "twist": "The thick dust and dense starlight of our own galactic core completely blocks our telescopes from seeing what lies at the center of the Great Attractor. We can measure its colossal gravitational hunger pulling our world, but we cannot see what is waiting for us.",
        "loop_cta": "What colossal cosmic monster is dragging our universe across the dark? Like this video and subscribe to our channel for daily cosmic mysteries."
    },
    {
        "id": "space_bootes_void",
        "category": "space",
        "motion_style": "ken_burns",
        "bgm_vibe": "space_tech",
        "title": "The Boötes Void: The Creepiest Empty Space in the Universe 🌌",
        "youtube_title": "The Terrifying 330-Million-Light-Year Void In Deep Space 🌌 #shorts #space #mystery #cosmos",
        "tags": ["space", "bootesvoid", "astronomy", "universe", "aliens", "science", "shorts", "viral"],
        "scenery_keywords": ["space", "cosmos", "stars"],
        "hook": "Imagine an area of space so vast and empty that if the Milky Way were inside it, we wouldn't have known other galaxies existed until the nineteen sixties.",
        "dilemma": "This is the Boötes Void, a spherical region of absolute darkness stretching over three hundred and thirty million light-years across. By normal cosmic density, it should contain over ten thousand galaxies.",
        "science": "Instead, astronomers have only found about sixty isolated galaxies scattered throughout this gargantuan expanse. It is one of the largest voids in the observable universe.",
        "twist": "Some astrophysicists and theorists playfully speculate whether an ancient Type Three civilization constructed massive Dyson spheres around thousands of star systems, completely blotting out their light from the outside universe.",
        "loop_cta": "Is the void empty by nature, or was it made dark on purpose? Like this video and subscribe to our channel for more unsolved mysteries of the cosmos."
    },
    {
        "id": "space_fermi_dark_forest",
        "category": "space",
        "motion_style": "ken_burns",
        "bgm_vibe": "space_tech",
        "title": "The Dark Forest Theory: Why The Universe Is Silent 🌲",
        "youtube_title": "Why We Should NEVER Broadcast Our Location To Space 🌲 #shorts #aliens #space #fermiparadox",
        "tags": ["space", "fermiparadox", "darkforest", "aliens", "scifi", "science", "shorts", "viral"],
        "scenery_keywords": ["space", "stars", "dark"],
        "hook": "Why has humanity never received a single radio signal from an alien civilization across billions of stars?",
        "dilemma": "The Dark Forest Theory provides the most chilling solution to the Fermi Paradox. Imagine the universe as a pitch-black forest at midnight.",
        "science": "Every intelligent civilization is like an armed hunter stalking silently through the trees. Because no civilization can ever be certain of another species' ultimate intentions, discovering another hunter's location makes them an existential threat.",
        "twist": "In this dark forest, the only logical survival strategy is absolute silence. The moment any civilization announces its presence to the cosmos, it is immediately wiped out by older, silent apex predators hiding in the dark.",
        "loop_cta": "Every time humanity beams messages into the stars, we might be lighting a flare in a dark forest. Like this video and subscribe to our channel for more cosmic reality checks."
    },
    {
        "id": "tech_dna_data_storage",
        "category": "abstract",
        "motion_style": "glitch_pop",
        "bgm_vibe": "space_tech",
        "title": "DNA Data Storage: Storing The Entire Internet in a Sugar Cube 🧬",
        "youtube_title": "How All Human Knowledge Can Fit In A Single Drop Of Liquid 🧬 #shorts #tech #future #science",
        "tags": ["technology", "dna", "futuretech", "computers", "science", "shorts", "viral"],
        "scenery_keywords": ["abstract", "neon", "futuristic"],
        "hook": "What if every movie, book, website, and photo ever created by humanity could fit inside a single teaspoon of liquid?",
        "dilemma": "Our current magnetic hard drives and silicon chips degrade within ten to twenty years. But nature perfected digital data storage over four billion years ago.",
        "science": "DNA stores information using four chemical bases: A, C, G, and T. Computer scientists have figured out how to translate digital binary zeros and ones directly into synthetic DNA molecules.",
        "twist": "A single gram of DNA can store over two hundred and fifteen petabytes of data — that is over two hundred million gigabytes — and it can remain completely intact for thousands of years without electricity.",
        "loop_cta": "The ultimate computer hard drive was already inside our cells all along. Hit like and subscribe to our channel for daily breakthroughs shaping the future of humanity."
    },

    # =========================================================================
    # 🏛️ CATEGORY 3: DEEP OCEAN, ANCIENT EARTH & NATURE MYSTERIES
    # (Audio: Cinematic Lofi, Soft Piano, Atmospheric Pads, Time Lapse Ambient)
    # (Motion: Ken Burns Scenic Drift, Smooth Wave Scale)
    # =========================================================================
    {
        "id": "ocean_colossal_squid_eyes",
        "category": "ocean",
        "motion_style": "ken_burns",
        "bgm_vibe": "nature_history_lofi",
        "title": "The Giant Eyes In The Deep Ocean Abyss 👁️",
        "youtube_title": "The Monster Eyes Watching You In The Deep Ocean Abyss 👁️ #shorts #ocean #nature #deepsea",
        "tags": ["ocean", "squid", "deepsea", "nature", "animals", "mystery", "shorts", "viral"],
        "scenery_keywords": ["ocean", "underwater", "sea"],
        "hook": "What living creature on planet Earth possesses eyes the exact size of dinner plates?",
        "dilemma": "Deep in the freezing sub-Antarctic waters, thousands of feet beneath the reach of sunlight, swims the colossal squid. Weighing over one thousand pounds with razor-sharp rotating hooks on its tentacles, it is the largest invertebrate on Earth.",
        "science": "Its eyes measure over thirty centimeters across — larger than a soccer ball. But why would an animal living in total pitch-black darkness need the largest eyes in animal history?",
        "twist": "Marine biologists discovered these colossal eyes are designed to detect the faint bioluminescent glow of microscopic organisms disturbed by incoming sperm whales hundreds of meters away. It literally uses living underwater neon to spot apex predators in the dark.",
        "loop_cta": "The ocean abyss contains monsters beyond our wildest nightmares. Like this video and subscribe to our channel for daily deep-sea discoveries."
    },
    {
        "id": "ocean_underwater_waterfalls",
        "category": "ocean",
        "motion_style": "ken_burns",
        "bgm_vibe": "nature_history_lofi",
        "title": "The Massive Waterfalls Flowing Beneath The Ocean 🌊",
        "youtube_title": "The Massive Underwater Waterfall 3 Miles Beneath The Ocean 🌊 #shorts #ocean #nature #science",
        "tags": ["ocean", "waterfall", "nature", "science", "earth", "geography", "shorts", "viral"],
        "scenery_keywords": ["ocean", "water", "sea"],
        "hook": "Did you know that the largest and most powerful waterfall on planet Earth is located completely underwater?",
        "dilemma": "Known as the Denmark Strait Cataract, this colossal cascade is located on the ocean floor between Greenland and Iceland. It plunges over three thousand five hundred meters down into the abyss — more than three times the height of Angel Falls.",
        "science": "It flows at an astonishing rate of over three million cubic meters of water per second, carrying more than two thousand times the volume of Niagara Falls. But how does water fall inside water?",
        "twist": "The cold Arctic water meeting warm Atlantic currents is significantly denser and heavier, causing trillions of tons of freezing polar water to plummet violently over a massive submarine cliff into the deep ocean floor.",
        "loop_cta": "Our oceans hold geological wonders that dwarf anything on land. Give this video a like and subscribe to our channel for more incredible Earth secrets."
    },
    {
        "id": "nature_blood_falls",
        "category": "nature",
        "motion_style": "ken_burns",
        "bgm_vibe": "nature_history_lofi",
        "title": "Blood Falls: The Crimson Mystery of Antarctica 🩸",
        "youtube_title": "The Terrifying Crimson Blood Falls In Antarctica 🩸 #shorts #nature #science #mystery",
        "tags": ["nature", "antarctica", "science", "mystery", "geology", "earth", "shorts", "viral"],
        "scenery_keywords": ["mountain", "lake", "nature"],
        "hook": "In the frozen Dry Valleys of Antarctica stands a five-story glacier pouring out a continuous stream of bright, crimson blood-red water.",
        "dilemma": "When Australian explorer Griffith Taylor discovered Blood Falls in nineteen eleven, early explorers believed red algae was staining the ice. But modern geochemistry uncovered a subterranean time capsule that rewrote science.",
        "science": "Beneath four hundred meters of solid glacial ice lies a subterranean hypersaline lake that has been completely sealed off from sunlight, oxygen, and the atmosphere for over two million years. Saturated with iron and ancient subterranean microbes, the water is three times saltier than seawater.",
        "twist": "The moment this trapped iron-rich water seeps through fissures and meets surface oxygen, it oxidizes instantly into rust, turning the waterfall into liquid crimson. Even more astonishing, ancient bacteria thrive in this pitch-black, oxygen-free lake, providing a direct blueprint for how alien life could survive under the ice of Jupiter's moon Europa.",
        "loop_cta": "Earth holds alien ecosystems locked under ancient ice. Tap like and subscribe to our channel to uncover extreme planetary wonders every single day."
    },
    {
        "id": "nature_sailing_stones",
        "category": "nature",
        "motion_style": "ken_burns",
        "bgm_vibe": "nature_history_lofi",
        "title": "The Sailing Stones of Death Valley 🪨",
        "youtube_title": "The Mystery of Rocks Moving Themselves Across The Desert 🪨 #shorts #nature #science #mystery",
        "tags": ["nature", "deathvalley", "mystery", "science", "geology", "facts", "shorts", "viral"],
        "scenery_keywords": ["valley", "nature", "mountain"],
        "hook": "In a remote dry lake bed in California's Death Valley, heavy boulders weighing hundreds of pounds move across the desert floor entirely on their own, leaving deep carved trails behind them.",
        "dilemma": "For over a century, no human had ever witnessed them move in person. Theories ranged from magnetic anomalies to hurricane winds and secret seismic vibrations.",
        "science": "In twenty fourteen, geologists finally solved the mystery using GPS trackers and time-lapse photography. On rare winter nights, brief rains form a shallow pool of water that freezes into paper-thin sheets of windowpane ice.",
        "twist": "As the morning sun warms the playa, the ice sheets fracture into floating panels. Light desert breezes then push the floating ice against the heavy rocks, gliding multi-hundred-pound boulders effortlessly across the slick mud at speeds of several inches per second.",
        "loop_cta": "Nature creates complex physical magic out of the simplest elements. Like this video and subscribe to our channel for more unsolved scientific revelations."
    },
    {
        "id": "nature_immortal_jellyfish",
        "category": "ocean",
        "motion_style": "ken_burns",
        "bgm_vibe": "nature_history_lofi",
        "title": "The Immortal Jellyfish: Biological Time Travel 🪼",
        "youtube_title": "The Only Living Creature That Can Never Die Of Old Age 🪼 #shorts #ocean #science #nature",
        "tags": ["ocean", "jellyfish", "biology", "immortality", "nature", "science", "shorts", "viral"],
        "scenery_keywords": ["ocean", "underwater", "nature"],
        "hook": "What if you could reset your biological age back to infancy whenever you got sick or grew old?",
        "dilemma": "There is a tiny sea creature known as Turritopsis dohrnii — the immortal jellyfish — that has achieved true biological immortality.",
        "science": "When faced with physical damage, starvation, or old age, this jellyfish does not die. Instead, it activates a rare cellular process called transdifferentiation. Its adult cells transform back into primitive stem cells, turning the jellyfish back into a juvenile polyp.",
        "twist": "It can repeat this cycle indefinitely, essentially living forever unless eaten by a predator. Geneticists are currently studying its genome to unlock cellular regeneration and anti-aging therapies for humans.",
        "loop_cta": "The secret to eternal life is already floating silently in our oceans. Like this video and subscribe to our channel for daily mind-blowing biological discoveries."
    },

    # =========================================================================
    # ⚡ CATEGORY 4: FAST-PACED & MIND-BLOWING REALITY ANOMALIES
    # (Audio: Phonk / Minimal Tech House, Glitch Hop, Fast Plucked Strings)
    # (Motion: Dynamic Beat Pulse, Zoom In / Out Wave, Pop-Up Visuals)
    # =========================================================================
    {
        "id": "trivia_cleopatra_pyramids_iphone",
        "category": "abstract",
        "motion_style": "beat_pulse",
        "bgm_vibe": "psychology_mystery",
        "title": "The Timeline Glitch: Cleopatra, The Pyramids, and The iPhone ⏳",
        "youtube_title": "Why Cleopatra Lived Closer To The iPhone Than The Pyramids ⏳ #shorts #history #facts #mindblown",
        "tags": ["history", "facts", "timeline", "cleopatra", "pyramids", "ancienthistory", "shorts", "viral"],
        "scenery_keywords": ["abstract", "ancient", "fantasy"],
        "hook": "Your perception of human history is completely warped, and this single fact will prove it in five seconds.",
        "dilemma": "When you picture ancient Egypt, you probably imagine Pharaohs like Cleopatra building the Great Pyramids of Giza at the exact same time.",
        "science": "In reality, the Great Pyramids were constructed around twenty-five hundred BC. Cleopatra was born around sixty-nine BC. That means over twenty-four hundred years passed between the Pyramids and Cleopatra.",
        "twist": "Cleopatra lived closer in time to the Moon Landing and the invention of the iPhone than she did to the construction of the Great Pyramids. To Cleopatra, the Pyramids were already ancient, mysterious ruins from an unknown ancient epoch.",
        "loop_cta": "Human history is far deeper and more ancient than school textbooks ever showed. Give this video a like and subscribe to our channel for mind-bending historical revelations."
    },
    {
        "id": "trivia_mantis_shrimp_vision",
        "category": "ocean",
        "motion_style": "beat_pulse",
        "bgm_vibe": "nature_history_lofi",
        "title": "The Mantis Shrimp: Seeing Colors Humans Can't Imagine 🌈",
        "youtube_title": "The Creature That Sees Colors Beyond Human Imagination 🌈 #shorts #ocean #nature #science",
        "tags": ["ocean", "animals", "science", "biology", "vision", "nature", "shorts", "viral"],
        "scenery_keywords": ["ocean", "underwater", "abstract"],
        "hook": "What if there are hundreds of vibrant colors in the world around you that your human eyes are completely blind to?",
        "dilemma": "Human eyes have three color photoreceptors: red, green, and blue. With these three channels, we can perceive about ten million distinct shades of color.",
        "science": "Now meet the mantis shrimp. This small ocean predator has sixteen distinct color photoreceptors, allowing it to see ultraviolet, infrared, and even circularly polarized light.",
        "twist": "Not only can it see a rainbow of colors that human brains cannot even conceive, but its punch accelerates at the speed of a twenty-two caliber bullet, boiling the surrounding water in a flash of underwater plasma.",
        "loop_cta": "The reality you see is only a tiny slice of the true universe. Hit like and subscribe to our channel for more hidden wonders of nature and biology."
    }
]


def get_curiosity_script_by_day(day_number: int) -> dict:
    """Returns a script for a given day (1-30+), cycling dynamically if exceeded."""
    idx = (day_number - 1) % len(CURIOSITY_TOPIC_BANK)
    raw = CURIOSITY_TOPIC_BANK[idx]
    
    # Assemble structured 1-to-2 minute narrative (150-180 words at natural speed = ~65-80s)
    full_narration = f"{raw['hook']} {raw['dilemma']} {raw['science']} {raw['twist']} {raw['loop_cta']}"
    
    return {
        "day": day_number,
        "id": raw["id"],
        "title": raw["title"],
        "youtube_title": raw["youtube_title"],
        "tags": raw["tags"],
        "category": raw["category"],
        "motion_style": raw.get("motion_style", "ken_burns"),
        "bgm_vibe": raw.get("bgm_vibe", "psychology_mystery"),
        "scenery_keywords": raw["scenery_keywords"],
        "narration": full_narration
    }


def generate_30_hour_curiosity_suite(total_hours: float = 30.0) -> list:
    """
    Builds a complete multi-day / multi-hour queue of curiosity scripts.
    For 30 hours, generates ~1,500 continuous high-retention video stories.
    """
    total_seconds_target = total_hours * 3600
    current_seconds = 0.0
    queue = []
    
    day = 1
    while current_seconds < total_seconds_target:
        script = get_curiosity_script_by_day(day)
        # Approximate duration: ~140 words per min
        words = len(script["narration"].split())
        est_duration = (words / 140.0) * 60.0
        current_seconds += est_duration
        queue.append(script)
        day += 1
        
    return queue


if __name__ == "__main__":
    print("=" * 70)
    print(f"  CURIOSITY SCRIPT MATRIX: {len(CURIOSITY_TOPIC_BANK)} Core High-Retention Master Kernels")
    print(f"  Sample Day 1 Script Word Count: {len(get_curiosity_script_by_day(1)['narration'].split())} words")
    suite = generate_30_hour_curiosity_suite(30.0)
    print(f"  30-Hour Marathon Total Scripts Generated: {len(suite)} shorts")
    print("=" * 70)


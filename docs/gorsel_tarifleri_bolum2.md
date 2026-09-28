# 2. Bölüm — Görsel tarifleri (ChatGPT)

## Nasıl kullanılır
1. ChatGPT'de yeni bir sohbet aç. Stil referansı olarak şu üç dosyayı yükle: `assets/raw/1A_peron.webp`, `assets/raw/A4_makas_kulubesi.webp`, `assets/raw/C2_duduk.webp`.
2. İlk mesajda **Ortak stil** paragrafını gönder, sonra tarifleri tek tek yapıştır. Her görseli ayrı mesajda iste.
3. Görseli indir ve verilen dosya adıyla `assets/raw/` klasörüne koy (`.png`, `.jpg` ya da `.webp` olabilir). GitHub'da **Add file → Upload files** ile yükleyebilirsin; dal olarak `claude/cloud-is4ttx`'i seç ya da `main`'e yükle, ben alırım.
4. Oyunda sahneler kodla griye çevrilir. Yine de görselleri **tam renkli** üret: tamir edilen yerlerde renk geri gelir.

Görsellerde **yazı, harf ve rakam olmamalı**; **yeşil bitki, yaprak ya da ağaç olmamalı** (dünyadaki her şey yanıp kül olmuştur). Tek istisna tohumun kendisidir.

## Ortak stil
```
Use the attached images as the exact style reference. Hand-drawn steampunk illustration in ink and watercolor on textured paper, like a Machinarium background. Rusty iron, riveted copper, verdigris and sepia tones, soft diffuse light, ash falling slowly like snow. Slightly crooked, storybook perspective. No people: the world is inhabited only by small, gentle, worn-out robots. Absolutely no text, letters, numbers or signage. No green plants, leaves or trees anywhere: everything living has burnt to ash long ago.
```

## Sahneler (yatay 16:9, 1536x1024 ya da daha geniş)
Sahneler oyunda tek ekran olarak kullanılır. Alt üçte biri, küçük bir robotun yürüyebileceği açık bir zemin olmalıdır; önemli nesneler zeminin arkasında ve iki yanında durmalıdır.

**A6_buhar_meydani**
```
Wide 16:9 scene: "Steam Square", a small cobbled square squeezed between gigantic rusty pipes and chimneys that fill the sky. In the center, a big copper boiler with a manifold of five hand-wheel valves in a row, each feeding a pipe of a different thickness; each pipe runs off to a different place: a tiny house chimney, a thick pipe climbing to a tall tower in the far right distance, a cracked leaking pipe next to a round door, a brass steam whistle on top, and an exhaust vent. On the left, the round riveted door of a tiny clockmaker's house built into a pipe, with a damp cracked brick wall beside it. Near the middle, a wrought-iron street lamp with an empty rope net trap hanging around its glass. Low eaves of little houses on the left with a dark crack under one eave. A warm pipe along the bottom right where a cat could sleep. A narrow alley opening on the right edge. Steam puffs, falling ash, empty open cobbles in the lower third.
```

**A7_nine_saat_evi**
```
Wide 16:9 interior: the tiny home of an old clockmaker robot, a cozy round room built inside a giant pipe. The walls are covered with dozens of stopped wall clocks of all sizes, all with blank faces. On the left, a worn velvet armchair, empty. On the right, a cluttered workbench with small enamel paint pots (clearly one blue pot and one yellow pot among others), brushes and clock hands. On the floor in the middle, a round iron floor grate with darkness below it. A tall grandfather-clock cabinet with a small drawer. A round door on the left edge. Dim warm lamp light, dust in the air, open floor in the lower third.
```

**A8_hurdaci_sokagi**
```
Wide 16:9 scene: "Scrapper's Alley", a narrow alley between tall pipe walls, packed with junk: springs, cogs, old boilers, bent sheet metal. Against the left wall, a sad heap of broken small stoker robots, each with an open coal hopper in its chest and soot stains, lying on top of each other. Along the right side, three rusty oil barrels spaced apart, big enough for a small robot to hide behind. A greasy rag hanging on a nail. A crowbar leaning against a crate. At the far end of the alley, a gap leading to the base of a tall tower, with a half-open metal shutter above the gap. Falling ash, smoke, open cobbles in the lower third.
```

**A9_asansor_kulesi**
```
Wide 16:9 interior: the base of a tall elevator tower. On the left, a birdcage-style iron elevator cabin standing on the ground. In the center, a huge wall of machinery with three empty gear axles arranged vertically (bottom, middle, top) and one very large bronze gear leaning on the floor beside it. A heavy counterweight hanging on a thick chain on the right. High up near the top of the frame, a small gear hanging from a hook, out of reach. On the wall, a faded engraved metal plate showing three gears of different sizes on three axles (drawing only, no text). A thick steam pipe entering from the left. Cables and a rope running up into darkness. Open floor in the lower third.
```

## Yakın çekimler (kare 1:1, 1254x1254)
**B8_vana_paneli**
```
Square close-up: a boiler valve manifold seen from the front. Five brass hand-wheel valves in a row, each on a pipe of a different thickness. Every pipe has a brass collar with notches engraved: some have one notch, some two, some three (notches only, no numbers). Above the row, the boiler's big round pressure gauge with a needle and a red zone on the right side (no numbers). Rust, rivets, warm light.
```

**B9_montaj_cizimi**
```
Square close-up: an old engraved metal plate on a riveted wall, showing a technical drawing of three gears stacked on three vertical axles: a big gear at the bottom, a small gear in the middle, a medium gear at the top; the gears' teeth are clearly countable. Drawing only, no text, no numbers. Scratched, stained, slightly faded.
```

**B10_disli_duvari**
```
Square close-up: a machinery wall with three empty gear axles arranged vertically (bottom, middle, top), each axle a polished steel shaft with a keyway, surrounded by rusty plates and rivets. Empty, no gears mounted.
```

**B12_gogus_kapagi_iki_yaprak**
```
Square close-up, exactly like the attached chest-window image (B7_gogus_kapagi_filiz): the round glass porthole on a small rusty robot's chest, opened, with soil inside. Now the sprout has grown into a young seedling with two fresh green leaves, glowing softly. The only green in the image.
```
(Bu tarif için `assets/raw/B7_gogus_kapagi_filiz.webp`'yi de yükle.)

## Karakter sayfaları (yatay, düz krem kâğıt zemin)
Her sayfada pozlar yan yana, aynı ölçekte, tam boy ve birbirine değmeden durmalıdır. Arka plan düz krem kâğıt; gölge sadece ayak altında. Oyunda bu pozlar otomatik kesilir.

**C7_nine_saat**
```
Character sheet on plain cream paper, 4 full-body poses side by side, same scale, not touching: "Granny Clock", an old gentle robot made from a wooden wall clock: round clock-face head with blank face and two little hands as eyebrows, a lace shawl, a small pendulum swinging under her body, thin brass legs. Pose 1: crying and searching the floor. Pose 2: standing, hands clasped, hopeful. Pose 3: winding something with a big key, happy. Pose 4: waving goodbye. No text.
```

**C8_torun**
```
Character sheet on plain cream paper, 2 full-body poses side by side, same scale: a tiny child robot made from a small alarm clock, with two bells on its head and a wind-up key hole in its back. Pose 1: sitting slumped and lifeless, eyes closed, as if sitting in an armchair (no chair drawn). Pose 2: standing, awake, happily waving both arms, bells ringing. No text.
```

**C9_vida_somun**
```
Character sheet on plain cream paper, 3 full-body poses side by side, same scale: twin scrap-collector robots, one tall and thin shaped like a screw, one short and round shaped like a hex nut. Pose 1: welded back to back by a crude weld seam, pulling in opposite directions and arguing (angry puffs). Pose 2: separated; the screw twin standing sadly, the nut twin slumped and switched off. Pose 3: still joined but now walking together on a third shared leg made of mismatched junk parts, both smiling. No text.
```

**C10_pirpir**
```
Character sheet on plain cream paper, 4 poses side by side, same scale: "Pirpir", a tiny pollinator drone like a bee, with a round tin body, striped copper bands, paper-and-tin wings, big curious lens eyes, thin wire legs. Pose 1: flying happily. Pose 2: tangled in a rope net, sad. Pose 3: carrying a small gear with its legs. Pose 4: circling a light bulb, enchanted. No text.
```

## Hafıza çizimleri ve efekt (kare 1:1)
**D4_hafiza_cizimi_2**
```
Square drawing on old torn paper, warm sepia with soft color, like a memory: the opening day of the Great Greenhouse long ago. Gardener robots with flowerpot heads and dry twigs, little helper robots, and an old barrel-organ robot playing music in front of the glass dome. The dome is full of plants and flowers (allowed here: this is the past). Festive, gentle.
```

**D5_hafiza_cizimi_3**
```
Square drawing on old torn paper, warm sepia with soft color, like a memory: gardener robots loading a last crate of seedlings in glass boxes onto a green steam train at a station platform; a round, mustached conductor robot with a cap and a whistle stands proudly by the train. Plants are allowed here (the past). Hopeful mood.
```

**D6_kivilcim**
```
Square image, dark and blurry like a sudden flash of memory: a wall of orange fire from a huge furnace, and in front of it silhouettes of many small stoker robots, each with a coal hopper in its chest, carrying shovels of coal in a line. Mostly black and deep orange, grainy, dreamlike. No text.
```

## Liste
| Dosya | Tür | Nerede |
|---|---|---|
| A6_buhar_meydani | sahne | 2a |
| A7_nine_saat_evi | sahne | 2b |
| A8_hurdaci_sokagi | sahne | 2c |
| A9_asansor_kulesi | sahne | 2d |
| B8_vana_paneli | yakın çekim | 2.1 |
| B9_montaj_cizimi | yakın çekim | 2.7 ipucu |
| B10_disli_duvari | yakın çekim | 2.7 |
| B12_gogus_kapagi_iki_yaprak | yakın çekim | bölüm sonu |
| C7_nine_saat | karakter | 2b |
| C8_torun | karakter | 2b |
| C9_vida_somun | karakter | 2c |
| C10_pirpir | karakter | 2a ve sonrası |
| D4_hafiza_cizimi_2 | hafıza | torun |
| D5_hafiza_cizimi_3 | hafıza | güvercin |
| D6_kivilcim | efekt | ilk şüphe |

Kül Toplayıcı (`C6_kul_toplayici`), Paşa Kedi ve Posta Güvercini mevcut görsellerle kullanılır.

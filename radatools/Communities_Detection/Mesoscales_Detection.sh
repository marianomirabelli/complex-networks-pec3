
echo ------------------------
echo --- Resistance range ---
echo ------------------------

./Mesoscales_Detection.exe  test-zachary_unwh.net  WN  trfr  0  1  1.0
./Mesoscales_Detection.exe  test-dolphins.net      WS  trfr  0  1  1.0

echo -----------------------------
echo --- Mesoscales min to max ---
echo -----------------------------

./Mesoscales_Detection.exe  test-zachary_unwh.net  WN  trfr  5  100  1.0
./Mesoscales_Detection.exe  test-dolphins.net      WS  trfr  5  100  5.0

echo -----------------------------
echo --- Mesoscales max to min ---
echo -----------------------------

./Mesoscales_Detection.exe  test-zachary_unwh.net  WN  -e+erfr  -1  100  1.0
./Mesoscales_Detection.exe  test-dolphins.net      WS  -e+erfr  -1  100  5.0

echo -----------

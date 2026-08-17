default(parisize, "64M");

E = ellinit([0, 0, 0, -32, 64]);
E0 = ellinit([0, 12, 0, 16, 0]);
Ehat = ellinit([0, -24, 0, 80, 0]);
Q = ellinit(ellfromeqn(y^2-(10*x^4-20*x^3+24*x^2-12*x+2)));

if (E.disc != 327680, error("unexpected E discriminant"));
if (E0.disc != 327680, error("unexpected E0 discriminant"));
if (Ehat.disc != 26214400, error("unexpected Ehat discriminant"));
if (Q.disc != 327680, error("unexpected corrected-quartic discriminant"));

print("PARI_VERSION=", version());
print("E_DISC=", E.disc);
print("E0_DISC=", E0.disc);
print("EHAT_DISC=", Ehat.disc);
print("Q_DISC=", Q.disc);
print("Q_MODEL=", Q[1..5]);
print("E_RANK=", ellrank(E));
print("E0_RANK=", ellrank(E0));
print("EHAT_RANK=", ellrank(Ehat));
print("Q_RANK=", ellrank(Q));
print("E_TORS=", elltors(E));
print("E0_TORS=", elltors(E0));
print("EHAT_TORS=", elltors(Ehat));
print("Q_TORS=", elltors(Q));
print("E_ONCURVE=", ellisoncurve(E, [0, 8]));
print("E_2P=", ellmul(E, [0, 8], 2));
print("E_4P=", ellmul(E, [0, 8], 4));
print("E0_MAP_POINT=", ellisoncurve(E0, [-4, 8]));
print("E0_2P=", ellmul(E0, [-4, 8], 2));
print("E0_4P=", ellmul(E0, [-4, 8], 4));
print("E_GLOBALRED=", ellglobalred(E));
print("E_2_ISO_CLASS=", ellisomat(E, 2, 1));

quit

int extgcd(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1, y = 0;
        return a;
    }
    int x1, y1;
    int tmp = extgcd(b, a % b, x1, y1);
    x = y1, y = x1 - (a / b) * y1;
    return tmp;
}

void solve() {
    int a, b, c;
    cin >> a >> b >> c;
    int x, y;
    int gcd = extgcd(a, b, x, y);
    if (c % gcd != 0) {
        cout << "No solutions\n";
    } else {
        int k = c / gcd;
        cout << x * k << ' ' << b / gcd << '\n'; // c' * x_0 + b' * k
        cout << y * k << ' ' << -(a / gcd) << '\n'; // c' * y_0 - a' * k
    }
}
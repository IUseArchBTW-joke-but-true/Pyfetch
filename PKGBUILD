pkgname=pyfetch
pkgver=0.1.0
pkgrel=1
pkgdesc="A simple system information fetch tool written in Python"
arch=('any')
url="https://github.com/IUseArchBTW-joke-but-true/Pyfetch"
license=('MIT')
depends=('python')
source=("https://github.com/IUseArchBTW-joke-but-true/Pyfetch/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('SKIP')

package() {
    install -Dm755 "$srcdir/Pyfetch-${pkgver}/main.py" \
        "$pkgdir/usr/share/pyfetch/main.py"

    install -Dm644 "$srcdir/Pyfetch-${pkgver}/LICENSE" \
        "$pkgdir/usr/share/licenses/pyfetch/LICENSE"

    install -d "$pkgdir/usr/bin"

    cat > "$pkgdir/usr/bin/pyfetch" <<'EOF'
#!/bin/sh
exec python /usr/share/pyfetch/main.py "$@"
EOF

    chmod 755 "$pkgdir/usr/bin/pyfetch"
}



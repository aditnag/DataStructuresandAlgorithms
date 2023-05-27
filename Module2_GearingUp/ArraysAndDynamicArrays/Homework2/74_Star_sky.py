class StarSky():
    def brightness(self, n, q, c, star, t, x1, y1, x2, y2):
        bcount = 0
        for i in range(n):
            time = t
            x = star[i][0]
            y = star[i][1]
            s = star[i][2]
            # bcount = s
            if x1 <= x <= x2 and y1 <= y <= y2:
                while time:
                    if s < c:
                        s += 1
                    elif s == c:
                        s = 0
                    time -= 1
                bcount += s
        return bcount


if __name__ == '__main__':
    obj = StarSky()
    n, q, c = list(map(int, input().strip().split()))[:3]
    star = []
    for i in range(n):
        star.append(list(map(int, input().strip().split()))[:3])

    for i in range(q):
        t, x1, y1, x2, y2 = list(map(int, input().strip().split()))[:5]
        max_brightness = obj.brightness(n, q, c, star, t, x1, y1, x2, y2)
        print(max_brightness)

class Reindeer:
    def __init__(self, speed, duration, rest):
        self.speed = speed
        self.duration = duration
        self.rest_length = rest
        self.is_resting = False
        self.time_rested = 0
        self.time_flying = 0
        self.distance = 0
        self.score = 0

    def fly(self):
        self.distance += self.speed
        self.time_flying += 1
        if self.time_flying == self.duration:
            self.is_resting = True
            self.time_rested = 0

    def rest(self):
        self.time_rested += 1
        if self.time_rested == self.rest_length:
            self.is_resting = False
            self.time_flying = 0

    def do_something(self):
        if self.is_resting:
            self.rest()
        else:
            self.fly()

if __name__ == '__main__':
    with open('input') as f:
        deer_properties = f.readlines()
        deer = {}
        for d in deer_properties:
            d = d.split(' ')
            deer[d[0]] = Reindeer(int(d[3]), int(d[6]), int(d[13]))

        for _ in range(2503):
            rankings = []
            for k,v in deer.items():
                v.do_something()
                rankings.append((v.distance,k))
            rankings.sort()
            deer[rankings[-1][1]].score += 1
            


        results1 = []
        results2 = []
        for k,v in deer.items():
            results1.append((v.distance, k))
            results2.append((v.score,k))
        results1.sort()
        results2.sort()
        print(f'part 1: {results1[-1]}')
        print(f'part 2: {results2[-1]}')
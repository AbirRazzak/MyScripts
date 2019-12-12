from typing import List, Any


class Coord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        return '<x={0:3}, y={1:3}, z={2:3}>'.format(self.x, self.y, self.z,)


class Moon:
    def __init__(self, pos: Coord, vel=Coord(0, 0, 0)):
        self.pos = pos
        self.vel = vel

    def display(self):
        return 'pos={}, vel={}'.format(self.pos.display(), self.vel.display())

    def potential(self):
        return abs(self.pos.x) + abs(self.pos.y) + abs(self.pos.z)

    def kinetic(self):
        return abs(self.vel.x) + abs(self.vel.y) + abs(self.vel.z)

    def energy(self):
        return self.potential() * self.kinetic()

    def display_energies(self):
        return 'pot: {0:6} + {1:6} + {2:6} = {3:6};\tkin: {4:6} + {5:6} + {6:6} = {7:6};\ttotal: {3:6} * {7:6} = {8:6}'\
            .format(abs(self.pos.x), abs(self.pos.y), abs(self.pos.z), self.potential(),
                   abs(self.vel.x), abs(self.vel.y), abs(self.vel.z), self.kinetic(),
                   self.energy())


def add_coords(c1: Coord, c2: Coord) -> Coord:
    x = c1.x + c2.x
    y = c1.y + c2.y
    z = c1.z + c2.z
    return Coord(x, y, z)


def calc_gravity(m1: Moon, m2: Moon) -> Coord:
    if m1.pos.x == m2.pos.x:
        vx = 0
    else:
        if m1.pos.x > m2.pos.x:
            vx = -1
        else:
            vx = 1

    if m1.pos.y == m2.pos.y:
        vy = 0
    else:
        if m1.pos.y > m2.pos.y:
            vy = -1
        else:
            vy = 1

    if m1.pos.z == m2.pos.z:
        vz = 0
    else:
        if m1.pos.z > m2.pos.z:
            vz = -1
        else:
            vz = 1

    return Coord(vx, vy, vz)


def calc_velocity(moons: List[Moon], i: int) -> Coord:
    m = moons[i]
    g = Coord(0, 0, 0)
    for foo in range(len(moons)):
        if not foo == i:
            g = add_coords(g, calc_gravity(m, moons[foo]))

    return g


def simulate_steps(moons: List[Moon], steps: int):
    print('After 0 steps')
    for m in moons:
        print(m.display())
    print('')

    for i in range(steps):
        print('After {} steps:'.format(i+1))
        new_moons = []
        for j in range(len(moons)):
            old_pos = moons[j].pos
            old_vel = moons[j].vel
            vel = calc_velocity(moons, j)

            new_vel = add_coords(old_vel, vel)
            new_pos = add_coords(old_pos, new_vel)
            new_moon = Moon(new_pos, new_vel)

            print(new_moon.display())
            new_moons.append(new_moon)
        print('')
        moons = new_moons

    print('Energy after {} steps:'.format(steps))
    m_energy: List[int] = []
    for m in moons:
        print(m.display_energies())
        m_energy.append(m.energy())

    sum: int = m_energy[0]
    energy_output = 'Sum of total energy: {}'.format(m_energy[0])
    for nrg in range(len(m_energy)):
        if not nrg == 0:
            sum += m_energy[nrg]
            energy_output += ' + {}'.format(m_energy[nrg])
    energy_output += ' = {}'.format(sum)
    print(energy_output)


if __name__ == '__main__':
    moons = [
        Moon(Coord(5, 4, 4)),
        Moon(Coord(-11, -11, -3)),
        Moon(Coord(0, 7, 0)),
        Moon(Coord(-13, 2, 10))
    ]
    simulate_steps(moons, 1000)

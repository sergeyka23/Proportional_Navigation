import Classes as Cls
import math
import random
import matplotlib.pyplot as plt

amount_of_tar = 2
N = 2
dk = 5
tar_lst = []
dist_to_tar = []
lamda_angle_of_target = [0.0, 0.0]
gamma_angle_to_target = [0.0, 0.0]
num_enabled = amount_of_tar + 1
delta_t = 0.5
list_of_excluded = []

# init all targets and a missile
missile = Cls.Missile
missile.a = 5

for i in range(amount_of_tar):
    tar = Cls.Target()
    #    tar[i].start_x = random.randrange(20)
    #    tar[i].start_y = random.randrange(20)
    tar.start_x = -50 + (i * 20)
    tar.start_y = -30 + (i * 20)
    tar.prev_x = tar.start_x
    tar.prev_y = tar.start_y
    tar.current_x = tar.start_x
    tar.current_y = tar.start_y
    tar.current_pos = [tar.current_x, tar.current_y]
    #    tar[i].start_ang = random.randrange(360)
    tar.start_ang = 45 + i * 20
    #    tar[i].v = random.randrange(10)
    tar.v = 5 + i * 2

    tar_lst.append(tar)
    dist_to_tar.append(math.dist(tar_lst[i].current_pos, missile.current_pos))
# find the closest target
i_min = dist_to_tar.index(min(dist_to_tar))

lamda_angle_of_target[0] = math.degrees(
    math.atan2((tar_lst[i_min].current_y - missile.current_y), (tar_lst[i_min].current_x - missile.current_x)))
gamma_angle_to_target[0] = lamda_angle_of_target[0]

while num_enabled != 0:

    for i in range(amount_of_tar):
        if tar_lst[i].enable and dk < dist_to_tar[i] and i not in list_of_excluded:
            tar_lst[i].current_x = tar_lst[i].prev_x + tar_lst[i].v * math.cos(math.radians(tar_lst[i].start_ang)) * delta_t
            tar_lst[i].current_y = tar_lst[i].prev_y + tar_lst[i].v * math.sin(math.radians(tar_lst[i].start_ang)) * delta_t
            tar_lst[i].prev_x = tar_lst[i].current_x
            tar_lst[i].prev_y = tar_lst[i].current_y
            tar_lst[i].current_pos = [tar_lst[i].current_x, tar_lst[i].current_y]
            missile.current_pos = [ missile.current_x,  missile.current_y]
            dist_to_tar[i] = math.dist(tar_lst[i].current_pos, missile.current_pos)
        elif dk >= dist_to_tar[i]:
            tar_lst[i].enable = False
            num_enabled = num_enabled - 1
            list_of_excluded.append(i)
            missile.current_vx = 0
            missile.current_vy = 0

        print("missile current_x: " + f'{missile.current_x:.1f}' + " current_y: " + f'{missile.current_y:.1f}' +
              " fpa[0]: " + f'{gamma_angle_to_target[0]:.1f}' + " fpa[1]: " + f'{gamma_angle_to_target[1]:.1f}' + " dist: " + f'{dist_to_tar[i_min]:.1f}')
        print(
            "target" + str(i) + " current_x: " + f'{tar_lst[i].current_x:.1f}' + " current_y: " + f'{tar_lst[i].current_y:1f}' +
            " los[0]: " + f'{lamda_angle_of_target[0]:.1f}' + " los[1]: " + f'{lamda_angle_of_target[1]:.1f}')
    lamda_angle_of_target[1] = math.degrees(math.atan2(math.radians(tar_lst[i_min].current_y - missile.current_y),
                                                       math.radians(tar_lst[i_min].current_x - missile.current_x)))
    gamma_angle_to_target[1] = N * (lamda_angle_of_target[1] - lamda_angle_of_target[0]) + gamma_angle_to_target[0]
    plt.plot(missile.current_x, missile.current_x, '+', color='black');
    plt.plot(tar_lst[0].current_x, tar_lst[0].current_y, 'o', color='red');
    plt.plot(tar_lst[1].current_x, tar_lst[1].current_y, '^', color='blue');
    plt.xlim([-80, 80])
    plt.ylim([-80, 80])
    plt.show()

    missile.current_vx = missile.prev_vx + missile.a * math.cos(math.radians(gamma_angle_to_target[1])) * delta_t
    missile.current_vy = missile.prev_vy + missile.a * math.sin(math.radians(gamma_angle_to_target[1])) * delta_t

    missile.current_x = missile.prev_x + missile.current_vx * delta_t + 0.5 * missile.a * math.cos(
        math.radians(gamma_angle_to_target[1])) * delta_t * delta_t
    missile.current_y = missile.prev_y + missile.current_vy * delta_t + 0.5 * missile.a * math.sin(
        math.radians(gamma_angle_to_target[1])) * delta_t * delta_t

    missile.prev_vx = missile.current_vx
    missile.prev_vy = missile.current_vy
    missile.prev_x = missile.current_x
    missile.prev_y = missile.current_y

# Created on 2017-1-28
#coding=utf-8
import os
os.environ['KERAS_BACKEND']='cntk'
import keras
import numpy as np
from keras.models import Sequential
from keras.optimizers import RMSprop

class DQNAgent:
    def __init__(self, env):
        self.env = env
        self.memory = []
        self.gamma = 0.9  # decay rate
        self.epsilon = 1  # exploration
        self.epsilon_decay = .995
        self.epsilon_min = 0.1
        self.learning_rate = 0.0001
        self._build_model()

    def _build_model(self):
        model = Sequential()
        from keras.layers import Dense
        model.add(Dense(128, input_dim=4, activation='tanh'))
        model.add(Dense(128, activation='tanh'))
        model.add(Dense(128, activation='tanh'))
        model.add(Dense(2, activation='linear'))
        model.compile(loss='mse',
                      optimizer=RMSprop(lr=self.learning_rate))
        self.model = model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return env.action_space.sample()
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # returns action

    def replay(self, batch_size):
        batches = min(batch_size, len(self.memory))
        batches = np.random.choice(len(self.memory), batches)
        for i in batches:
            state, action, reward, next_state, done = self.memory[i]
            target = reward
            if not done:
                target = reward + self.gamma * \
                                  np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, nb_epoch=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

if __name__ == "__main__":
    # 为agent初始化gym环境参数
    env = gym.make('CartPole-v0')
    agent = DQNAgent(env)

    # 游戏的主循环
    for e in range(episodes):

        # 在每次游戏开始时复位状态参数
        state = env.reset()
        state = np.reshape(state, [1, 4])

        # time_t 代表游戏的每一帧
        # 我们的目标是使得杆子尽可能长地保持竖直朝上
        # time_t 越大，分数越高
        for time_t in range(5000):
            # turn this on if you want to render
            # env.render()

            # 选择行为
            action = agent.act(state)

            # 在环境中施加行为推动游戏进行
            next_state, reward, done, _ = env.step(action)
            next_state = np.reshape(next_state, [1, 4])

            # reward缺省为1
            # 在每一个agent完成了目标的帧agent都会得到回报
            # 并且如果失败得到-100
            reward = -100 if done else reward

            # 记忆先前的状态，行为，回报与下一个状态
            agent.remember(state, action, reward, next_state, done)

            # 使下一个状态成为下一帧的新状态
            state = copy.deepcopy(next_state)

            # 如果游戏结束done被置为ture
            # 除非agent没有完成目标
            if done:
                # 打印分数并且跳出游戏循环
                print("episode: {}/{}, score: {}"
                      .format(e, episodes, time_t))
                break
        # 通过之前的经验训练模型
        agent.replay(32)


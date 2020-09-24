# -*- coding: utf-8 -*-
"""
This system uses a transition matrix and the Turtle module to create a visualized walk-through
of my mental state over the course of a day. My mood upon waking is determined at random, and
the following four moods over the course of the day are determined using probabilities based on
the previous state, as is standard in a first order Markov chain. At each mood change, the Turtle
module draws the corresponding shape to visually represent that mood, resulting in a piece of art
with five shapes representing my head space over the course of the day.

Irene Lunt
September 24, 2020
"""
import turtle
import random as rand

# defines the state space
states = ["Happy", "Sad", "Anxious", "Motivated", "Blah"]

# transition matrix
# indexes align with those of states array
transition_matrix = [[0.3, 0.1, 0.1, 0.4, 0.1], [0.1, 0.2, 0.3, 0.1, 0.3],
                     [0.1, 0.1, 0.4, 0.1, 0.3], [0.4, 0.1, 0.2, 0.2, 0.1],
                     [0.1, 0.2, 0.4, 0.1, 0.3]]


def get_next_state(state):
    """ This function creates an array of states based on the
    probabilities in transition_matrix and uses this array
    to select the next state

    :param state: The current state
    :type state: string
    :returns: string -- the next state
    """
    prob_array = []
    i = 0
    # Based on transition matrix, adds each state x times to fill array
    for x in transition_matrix[states.index(state)]:
        p = int(x * 10)
        j = 0
        while j < p:
            prob_array.append(states[i])
            j += 1
        i += 1
    next_state = prob_array[rand.randint(0, 9)]
    return next_state


# instantiates turtle window and Turtle
scr = turtle.Screen()
tut = turtle.Turtle()
tut.hideturtle()    # makes turtle hidden for drawing purposes


def move_tut():
    """ Randomly moves turtle to new place in window """
    tut.penup()
    tut.goto(rand.randint(-150, 150), rand.randint(-150, 150))


def draw_happy():
    """ Draws visual representation of "Happy" state """
    tut.pen(pencolor="pink", pensize=10)
    tut.pendown()
    for i in range(6):
        tut.forward(100)
        tut.right(60)


def draw_sad():
    """ Draws visual representation of "Sad" state """
    tut.pen(pencolor="blue", pensize=10)
    tut.pendown()
    for i in range(3):
        tut.forward(150)
        tut.right(120)


def draw_anxious():
    """ Draws visual representation of "Anxious" state """
    tut.pen(pencolor="violet", pensize=5)
    tut.pendown()
    for i in range(100):
        tut.fd(3 + i / 4)
        tut.right(15)


def draw_motivated():
    """ Draws visual representation of "Motivated" state """
    tut.pen(pencolor="orange", pensize=7)
    tut.pendown()
    for i in range(12):
        tut.fd(150)
        tut.bk(150)
        tut.right(30)


def draw_blah():
    """ Draws visual representation of "Blah" state """
    tut.pen(pencolor="gray", pensize=8)
    tut.pendown()
    tut.circle(100)


def draw_next(state):
    """ Calls method needed to draw given state

    :param state: state to draw
    :type state: string
    """
    move_tut()
    if state == "Happy":
        draw_happy()
    elif state == "Sad":
        draw_sad()
    elif state == "Anxious":
        draw_anxious()
    elif state == "Motivated":
        draw_motivated()
    else:
        draw_blah()


def main():
    current_state = states[rand.randint(0, 4)]  # start state is random
    print("start state: " + current_state)
    draw_next(current_state)

    for i in range(4):
        current_state = get_next_state(current_state)
        print("next_state: " + current_state)
        draw_next(current_state)

    scr.exitonclick()


if __name__ == "__main__":
    main()

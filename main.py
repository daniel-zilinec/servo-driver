import machine
from machine import Pin, ADC
import utime

SERVO_DUTY_MIN = 2500
SERVO_DUTY_MAX = 9000
SERVO_DUTY_DELTA = SERVO_DUTY_MAX - SERVO_DUTY_MIN

potentiometer_value = machine.ADC(26)
servo_pwm = machine.PWM(Pin(12))

def servo_init(servo):
    servo.freq(50)
    servo.duty_u16(0)

def servo_set(servo, value):
    duty = SERVO_DUTY_MIN + int(SERVO_DUTY_DELTA * value)
    print(f"Input: {value}, duty: {duty}")
    servo.duty_u16(duty)


servo_init(servo_pwm)
while True:
    pot_input  = potentiometer_value.read_u16() / 65535

    servo_set(servo_pwm, pot_input)
    utime.sleep(0.1)
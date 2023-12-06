# # from machine import I2C
# import LSM6DSO
# import smbus

# bus = smbus.SMBus(1)

# # i2c = I2C(1)
# while True:
# 	i2c = bus
# 	lsm = LSM6DSO.LSM6DSO(i2c)
# 	lsm.ax()
# 	lsm.get_a()
# 	lsm.get()
# 	print(lsm.ax())
# from machine import I2C

import smbus
import time


import smbus
import time

# LSM6DSO I2C address
LSM6DSO_ADDRESS = 0x6B

# Register addresses for accelerometer
CTRL1_XL = 0x10
OUTX_L_XL = 0x28
OUTX_H_XL = 0x29
OUTY_L_XL = 0x2A
OUTY_H_XL = 0x2B
OUTZ_L_XL = 0x2C
OUTZ_H_XL = 0x2D

# Register addresses for gyroscope
CTRL2_G = 0x11
OUTX_L_G = 0x22
OUTX_H_G = 0x23
OUTY_L_G = 0x24
OUTY_H_G = 0x25
OUTZ_L_G = 0x26
OUTZ_H_G = 0x27

# Full-scale range and resolution for accelerometer
ACCEL_FULL_SCALE_RANGE_G = 2
ACCEL_RESOLUTION = 0.061  # mg/digit

# Full-scale range and resolution for gyroscope
GYRO_FULL_SCALE_RANGE_DPS = 2000
GYRO_RESOLUTION = 0.07  # mdps/digit

# Create an I2C bus object
bus = smbus.SMBus(1)  # Use 0 for older Raspberry Pi boards

# Initialize LSM6DSO accelerometer and gyroscope
bus.write_byte_data(LSM6DSO_ADDRESS, CTRL1_XL, 0x40)  # Set accelerometer to 2g full scale
bus.write_byte_data(LSM6DSO_ADDRESS, CTRL2_G, 0x40)    # Set gyroscope to 2000 dps full scale

try:
    while True:
        # Read accelerometer data
        x_l = bus.read_byte_data(LSM6DSO_ADDRESS, OUTX_L_XL)
        x_h = bus.read_byte_data(LSM6DSO_ADDRESS, OUTX_H_XL)
        y_l = bus.read_byte_data(LSM6DSO_ADDRESS, OUTY_L_XL)
        y_h = bus.read_byte_data(LSM6DSO_ADDRESS, OUTY_H_XL)
        z_l = bus.read_byte_data(LSM6DSO_ADDRESS, OUTZ_L_XL)
        z_h = bus.read_byte_data(LSM6DSO_ADDRESS, OUTZ_H_XL)

        # Combine low and high bytes for accelerometer
        x_acc = (x_h << 8 | x_l) >> 4
        y_acc = (y_h << 8 | y_l) >> 4
        z_acc = (z_h << 8 | z_l) >> 4

        # Convert to signed values for accelerometer
        x_acc = x_acc if x_acc < 0x800 else x_acc - 0x1000
        y_acc = y_acc if y_acc < 0x800 else y_acc - 0x1000
        z_acc = z_acc if z_acc < 0x800 else z_acc - 0x1000

        # Convert acceleration values to m/s^2
        x_acc_mps2 = x_acc * ACCEL_RESOLUTION * ACCEL_FULL_SCALE_RANGE_G * 9.81
        y_acc_mps2 = y_acc * ACCEL_RESOLUTION * ACCEL_FULL_SCALE_RANGE_G * 9.81
        z_acc_mps2 = z_acc * ACCEL_RESOLUTION * ACCEL_FULL_SCALE_RANGE_G * 9.81

        # Read gyroscope data
        x_l = bus.read_byte_data(LSM6DSO_ADDRESS, OUTX_L_G)
        x_h = bus.read_byte_data(LSM6DSO_ADDRESS, OUTX_H_G)
        y_l = bus.read_byte_data(LSM6DSO_ADDRESS, OUTY_L_G)
        y_h = bus.read_byte_data(LSM6DSO_ADDRESS, OUTY_H_G)
        z_l = bus.read_byte_data(LSM6DSO_ADDRESS, OUTZ_L_G)
        z_h = bus.read_byte_data(LSM6DSO_ADDRESS, OUTZ_H_G)

        # Combine low and high bytes for gyroscope
        x_gyro = (x_h << 8 | x_l) >> 4
        y_gyro = (y_h << 8 | y_l) >> 4
        z_gyro = (z_h << 8 | z_l) >> 4

        # Convert to signed values for gyroscope
        x_gyro = x_gyro if x_gyro < 0x800 else x_gyro - 0x1000
        y_gyro = y_gyro if y_gyro < 0x800 else y_gyro - 0x1000
        z_gyro = z_gyro if z_gyro < 0x800 else z_gyro - 0x1000

        # Convert gyroscope values to degrees per second
        x_gyro_dps = x_gyro * GYRO_RESOLUTION * GYRO_FULL_SCALE_RANGE_DPS
        y_gyro_dps = y_gyro * GYRO_RESOLUTION * GYRO_FULL_SCALE_RANGE_DPS
        z_gyro_dps = z_gyro * GYRO_RESOLUTION * GYRO_FULL_SCALE_RANGE_DPS

        # Print accelerometer and gyroscope values
        print(f"Acceleration (m/s^2) - X: {x_acc_mps2:.2f}   Y: {y_acc_mps2:.2f}   Z: {z_acc_mps2:.2f}")
        print(f"Gyroscope (dps) - X: {x_gyro_dps:.2f}   Y: {y_gyro_dps:.2f}   Z: {z_gyro_dps:.2f}")

        # Wait for a short period before reading again
        time.sleep(0.1)

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    pass

finally:
    # Cleanup
    bus.close()

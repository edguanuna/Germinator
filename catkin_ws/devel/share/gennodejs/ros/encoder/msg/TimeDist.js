// Auto-generated. Do not edit!

// (in-package encoder.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class TimeDist {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.timestamp = null;
      this.distanceLeft = null;
      this.distanceRight = null;
    }
    else {
      if (initObj.hasOwnProperty('timestamp')) {
        this.timestamp = initObj.timestamp
      }
      else {
        this.timestamp = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('distanceLeft')) {
        this.distanceLeft = initObj.distanceLeft
      }
      else {
        this.distanceLeft = 0.0;
      }
      if (initObj.hasOwnProperty('distanceRight')) {
        this.distanceRight = initObj.distanceRight
      }
      else {
        this.distanceRight = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TimeDist
    // Serialize message field [timestamp]
    bufferOffset = _serializer.time(obj.timestamp, buffer, bufferOffset);
    // Serialize message field [distanceLeft]
    bufferOffset = _serializer.float64(obj.distanceLeft, buffer, bufferOffset);
    // Serialize message field [distanceRight]
    bufferOffset = _serializer.float64(obj.distanceRight, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TimeDist
    let len;
    let data = new TimeDist(null);
    // Deserialize message field [timestamp]
    data.timestamp = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [distanceLeft]
    data.distanceLeft = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [distanceRight]
    data.distanceRight = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'encoder/TimeDist';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3a8d79d031810f535ef4e5c20861539b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # TimeDist.msg
    time timestamp
    float64 distanceLeft
    float64 distanceRight
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TimeDist(null);
    if (msg.timestamp !== undefined) {
      resolved.timestamp = msg.timestamp;
    }
    else {
      resolved.timestamp = {secs: 0, nsecs: 0}
    }

    if (msg.distanceLeft !== undefined) {
      resolved.distanceLeft = msg.distanceLeft;
    }
    else {
      resolved.distanceLeft = 0.0
    }

    if (msg.distanceRight !== undefined) {
      resolved.distanceRight = msg.distanceRight;
    }
    else {
      resolved.distanceRight = 0.0
    }

    return resolved;
    }
};

module.exports = TimeDist;

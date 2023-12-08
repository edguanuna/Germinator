// Auto-generated. Do not edit!

// (in-package perception.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class CentroidsArray {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.centroids = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('centroids')) {
        this.centroids = initObj.centroids
      }
      else {
        this.centroids = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CentroidsArray
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [centroids]
    // Serialize the length for message field [centroids]
    bufferOffset = _serializer.uint32(obj.centroids.length, buffer, bufferOffset);
    obj.centroids.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CentroidsArray
    let len;
    let data = new CentroidsArray(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [centroids]
    // Deserialize array length for message field [centroids]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.centroids = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.centroids[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 24 * object.centroids.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'perception/CentroidsArray';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6fdfa26afed9c608e923375eed94abe0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # File: perception/msg/CentroidsArray.msg
    Header header
    geometry_msgs/Point[] centroids
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CentroidsArray(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.centroids !== undefined) {
      resolved.centroids = new Array(msg.centroids.length);
      for (let i = 0; i < resolved.centroids.length; ++i) {
        resolved.centroids[i] = geometry_msgs.msg.Point.Resolve(msg.centroids[i]);
      }
    }
    else {
      resolved.centroids = []
    }

    return resolved;
    }
};

module.exports = CentroidsArray;

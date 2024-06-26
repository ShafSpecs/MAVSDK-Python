# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gimbal/gimbal.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13gimbal/gimbal.proto\x12\x11mavsdk.rpc.gimbal\x1a\x14mavsdk_options.proto\"H\n\x10SetAnglesRequest\x12\x10\n\x08roll_deg\x18\x01 \x01(\x02\x12\x11\n\tpitch_deg\x18\x02 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x03 \x01(\x02\"K\n\x11SetAnglesResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\";\n\x15SetPitchAndYawRequest\x12\x11\n\tpitch_deg\x18\x01 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x02 \x01(\x02\"P\n\x16SetPitchAndYawResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"Q\n\x1dSetPitchRateAndYawRateRequest\x12\x18\n\x10pitch_rate_deg_s\x18\x01 \x01(\x02\x12\x16\n\x0eyaw_rate_deg_s\x18\x02 \x01(\x02\"X\n\x1eSetPitchRateAndYawRateResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"D\n\x0eSetModeRequest\x12\x32\n\x0bgimbal_mode\x18\x01 \x01(\x0e\x32\x1d.mavsdk.rpc.gimbal.GimbalMode\"I\n\x0fSetModeResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"X\n\x15SetRoiLocationRequest\x12\x14\n\x0clatitude_deg\x18\x01 \x01(\x01\x12\x15\n\rlongitude_deg\x18\x02 \x01(\x01\x12\x12\n\naltitude_m\x18\x03 \x01(\x02\"P\n\x16SetRoiLocationResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"J\n\x12TakeControlRequest\x12\x34\n\x0c\x63ontrol_mode\x18\x01 \x01(\x0e\x32\x1e.mavsdk.rpc.gimbal.ControlMode\"M\n\x13TakeControlResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"\x17\n\x15ReleaseControlRequest\"P\n\x16ReleaseControlResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"\x19\n\x17SubscribeControlRequest\"K\n\x0f\x43ontrolResponse\x12\x38\n\x0e\x63ontrol_status\x18\x01 \x01(\x0b\x32 .mavsdk.rpc.gimbal.ControlStatus\"\\\n\nQuaternion\x12\x12\n\x01w\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x12\n\x01x\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x12\n\x01y\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x12\n\x01z\x18\x04 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"]\n\nEulerAngle\x12\x19\n\x08roll_deg\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1a\n\tpitch_deg\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x18\n\x07yaw_deg\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"l\n\x13\x41ngularVelocityBody\x12\x1b\n\nroll_rad_s\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1c\n\x0bpitch_rad_s\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1a\n\tyaw_rad_s\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"\xcc\x02\n\x08\x41ttitude\x12:\n\x13\x65uler_angle_forward\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.gimbal.EulerAngle\x12\x39\n\x12quaternion_forward\x18\x02 \x01(\x0b\x32\x1d.mavsdk.rpc.gimbal.Quaternion\x12\x38\n\x11\x65uler_angle_north\x18\x03 \x01(\x0b\x32\x1d.mavsdk.rpc.gimbal.EulerAngle\x12\x37\n\x10quaternion_north\x18\x04 \x01(\x0b\x32\x1d.mavsdk.rpc.gimbal.Quaternion\x12@\n\x10\x61ngular_velocity\x18\x05 \x01(\x0b\x32&.mavsdk.rpc.gimbal.AngularVelocityBody\x12\x14\n\x0ctimestamp_us\x18\x06 \x01(\x04\"\x1a\n\x18SubscribeAttitudeRequest\"A\n\x10\x41ttitudeResponse\x12-\n\x08\x61ttitude\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.gimbal.Attitude\"\xc7\x01\n\rControlStatus\x12\x34\n\x0c\x63ontrol_mode\x18\x01 \x01(\x0e\x32\x1e.mavsdk.rpc.gimbal.ControlMode\x12\x1d\n\x15sysid_primary_control\x18\x02 \x01(\x05\x12\x1e\n\x16\x63ompid_primary_control\x18\x03 \x01(\x05\x12\x1f\n\x17sysid_secondary_control\x18\x04 \x01(\x05\x12 \n\x18\x63ompid_secondary_control\x18\x05 \x01(\x05\"\xe1\x01\n\x0cGimbalResult\x12\x36\n\x06result\x18\x01 \x01(\x0e\x32&.mavsdk.rpc.gimbal.GimbalResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x84\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x10\n\x0cRESULT_ERROR\x10\x02\x12\x12\n\x0eRESULT_TIMEOUT\x10\x03\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x04\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x05*B\n\nGimbalMode\x12\x1a\n\x16GIMBAL_MODE_YAW_FOLLOW\x10\x00\x12\x18\n\x14GIMBAL_MODE_YAW_LOCK\x10\x01*Z\n\x0b\x43ontrolMode\x12\x15\n\x11\x43ONTROL_MODE_NONE\x10\x00\x12\x18\n\x14\x43ONTROL_MODE_PRIMARY\x10\x01\x12\x1a\n\x16\x43ONTROL_MODE_SECONDARY\x10\x02\x32\xac\x07\n\rGimbalService\x12X\n\tSetAngles\x12#.mavsdk.rpc.gimbal.SetAnglesRequest\x1a$.mavsdk.rpc.gimbal.SetAnglesResponse\"\x00\x12g\n\x0eSetPitchAndYaw\x12(.mavsdk.rpc.gimbal.SetPitchAndYawRequest\x1a).mavsdk.rpc.gimbal.SetPitchAndYawResponse\"\x00\x12\x7f\n\x16SetPitchRateAndYawRate\x12\x30.mavsdk.rpc.gimbal.SetPitchRateAndYawRateRequest\x1a\x31.mavsdk.rpc.gimbal.SetPitchRateAndYawRateResponse\"\x00\x12R\n\x07SetMode\x12!.mavsdk.rpc.gimbal.SetModeRequest\x1a\".mavsdk.rpc.gimbal.SetModeResponse\"\x00\x12g\n\x0eSetRoiLocation\x12(.mavsdk.rpc.gimbal.SetRoiLocationRequest\x1a).mavsdk.rpc.gimbal.SetRoiLocationResponse\"\x00\x12^\n\x0bTakeControl\x12%.mavsdk.rpc.gimbal.TakeControlRequest\x1a&.mavsdk.rpc.gimbal.TakeControlResponse\"\x00\x12g\n\x0eReleaseControl\x12(.mavsdk.rpc.gimbal.ReleaseControlRequest\x1a).mavsdk.rpc.gimbal.ReleaseControlResponse\"\x00\x12\x66\n\x10SubscribeControl\x12*.mavsdk.rpc.gimbal.SubscribeControlRequest\x1a\".mavsdk.rpc.gimbal.ControlResponse\"\x00\x30\x01\x12i\n\x11SubscribeAttitude\x12+.mavsdk.rpc.gimbal.SubscribeAttitudeRequest\x1a#.mavsdk.rpc.gimbal.AttitudeResponse\"\x00\x30\x01\x42\x1f\n\x10io.mavsdk.gimbalB\x0bGimbalProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gimbal.gimbal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020io.mavsdk.gimbalB\013GimbalProto'
  _globals['_QUATERNION'].fields_by_name['w']._loaded_options = None
  _globals['_QUATERNION'].fields_by_name['w']._serialized_options = b'\202\265\030\003NaN'
  _globals['_QUATERNION'].fields_by_name['x']._loaded_options = None
  _globals['_QUATERNION'].fields_by_name['x']._serialized_options = b'\202\265\030\003NaN'
  _globals['_QUATERNION'].fields_by_name['y']._loaded_options = None
  _globals['_QUATERNION'].fields_by_name['y']._serialized_options = b'\202\265\030\003NaN'
  _globals['_QUATERNION'].fields_by_name['z']._loaded_options = None
  _globals['_QUATERNION'].fields_by_name['z']._serialized_options = b'\202\265\030\003NaN'
  _globals['_EULERANGLE'].fields_by_name['roll_deg']._loaded_options = None
  _globals['_EULERANGLE'].fields_by_name['roll_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_EULERANGLE'].fields_by_name['pitch_deg']._loaded_options = None
  _globals['_EULERANGLE'].fields_by_name['pitch_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_EULERANGLE'].fields_by_name['yaw_deg']._loaded_options = None
  _globals['_EULERANGLE'].fields_by_name['yaw_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['roll_rad_s']._loaded_options = None
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['roll_rad_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['pitch_rad_s']._loaded_options = None
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['pitch_rad_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['yaw_rad_s']._loaded_options = None
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['yaw_rad_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_GIMBALMODE']._serialized_start=2373
  _globals['_GIMBALMODE']._serialized_end=2439
  _globals['_CONTROLMODE']._serialized_start=2441
  _globals['_CONTROLMODE']._serialized_end=2531
  _globals['_SETANGLESREQUEST']._serialized_start=64
  _globals['_SETANGLESREQUEST']._serialized_end=136
  _globals['_SETANGLESRESPONSE']._serialized_start=138
  _globals['_SETANGLESRESPONSE']._serialized_end=213
  _globals['_SETPITCHANDYAWREQUEST']._serialized_start=215
  _globals['_SETPITCHANDYAWREQUEST']._serialized_end=274
  _globals['_SETPITCHANDYAWRESPONSE']._serialized_start=276
  _globals['_SETPITCHANDYAWRESPONSE']._serialized_end=356
  _globals['_SETPITCHRATEANDYAWRATEREQUEST']._serialized_start=358
  _globals['_SETPITCHRATEANDYAWRATEREQUEST']._serialized_end=439
  _globals['_SETPITCHRATEANDYAWRATERESPONSE']._serialized_start=441
  _globals['_SETPITCHRATEANDYAWRATERESPONSE']._serialized_end=529
  _globals['_SETMODEREQUEST']._serialized_start=531
  _globals['_SETMODEREQUEST']._serialized_end=599
  _globals['_SETMODERESPONSE']._serialized_start=601
  _globals['_SETMODERESPONSE']._serialized_end=674
  _globals['_SETROILOCATIONREQUEST']._serialized_start=676
  _globals['_SETROILOCATIONREQUEST']._serialized_end=764
  _globals['_SETROILOCATIONRESPONSE']._serialized_start=766
  _globals['_SETROILOCATIONRESPONSE']._serialized_end=846
  _globals['_TAKECONTROLREQUEST']._serialized_start=848
  _globals['_TAKECONTROLREQUEST']._serialized_end=922
  _globals['_TAKECONTROLRESPONSE']._serialized_start=924
  _globals['_TAKECONTROLRESPONSE']._serialized_end=1001
  _globals['_RELEASECONTROLREQUEST']._serialized_start=1003
  _globals['_RELEASECONTROLREQUEST']._serialized_end=1026
  _globals['_RELEASECONTROLRESPONSE']._serialized_start=1028
  _globals['_RELEASECONTROLRESPONSE']._serialized_end=1108
  _globals['_SUBSCRIBECONTROLREQUEST']._serialized_start=1110
  _globals['_SUBSCRIBECONTROLREQUEST']._serialized_end=1135
  _globals['_CONTROLRESPONSE']._serialized_start=1137
  _globals['_CONTROLRESPONSE']._serialized_end=1212
  _globals['_QUATERNION']._serialized_start=1214
  _globals['_QUATERNION']._serialized_end=1306
  _globals['_EULERANGLE']._serialized_start=1308
  _globals['_EULERANGLE']._serialized_end=1401
  _globals['_ANGULARVELOCITYBODY']._serialized_start=1403
  _globals['_ANGULARVELOCITYBODY']._serialized_end=1511
  _globals['_ATTITUDE']._serialized_start=1514
  _globals['_ATTITUDE']._serialized_end=1846
  _globals['_SUBSCRIBEATTITUDEREQUEST']._serialized_start=1848
  _globals['_SUBSCRIBEATTITUDEREQUEST']._serialized_end=1874
  _globals['_ATTITUDERESPONSE']._serialized_start=1876
  _globals['_ATTITUDERESPONSE']._serialized_end=1941
  _globals['_CONTROLSTATUS']._serialized_start=1944
  _globals['_CONTROLSTATUS']._serialized_end=2143
  _globals['_GIMBALRESULT']._serialized_start=2146
  _globals['_GIMBALRESULT']._serialized_end=2371
  _globals['_GIMBALRESULT_RESULT']._serialized_start=2239
  _globals['_GIMBALRESULT_RESULT']._serialized_end=2371
  _globals['_GIMBALSERVICE']._serialized_start=2534
  _globals['_GIMBALSERVICE']._serialized_end=3474
# @@protoc_insertion_point(module_scope)

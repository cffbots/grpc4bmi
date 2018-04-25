# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import bmi_pb2 as bmi__pb2


class BmiServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.initialize = channel.unary_unary(
        '/bmi.BmiService/initialize',
        request_serializer=bmi__pb2.InitializeRequest.SerializeToString,
        response_deserializer=bmi__pb2.Empty.FromString,
        )
    self.update = channel.unary_unary(
        '/bmi.BmiService/update',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.Empty.FromString,
        )
    self.updateUntil = channel.unary_unary(
        '/bmi.BmiService/updateUntil',
        request_serializer=bmi__pb2.UpdateUntilRequest.SerializeToString,
        response_deserializer=bmi__pb2.Empty.FromString,
        )
    self.updateFrac = channel.unary_unary(
        '/bmi.BmiService/updateFrac',
        request_serializer=bmi__pb2.UpdateFracRequest.SerializeToString,
        response_deserializer=bmi__pb2.Empty.FromString,
        )
    self.finalize = channel.unary_unary(
        '/bmi.BmiService/finalize',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.Empty.FromString,
        )
    self.runModel = channel.unary_unary(
        '/bmi.BmiService/runModel',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.Empty.FromString,
        )
    self.getComponentName = channel.unary_unary(
        '/bmi.BmiService/getComponentName',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.GetComponentNameResponse.FromString,
        )
    self.getInputVarNameCount = channel.unary_unary(
        '/bmi.BmiService/getInputVarNameCount',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.GetVarNameCountResponse.FromString,
        )
    self.getOutputVarNameCount = channel.unary_unary(
        '/bmi.BmiService/getOutputVarNameCount',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.GetVarNameCountResponse.FromString,
        )
    self.getInputVarNames = channel.unary_unary(
        '/bmi.BmiService/getInputVarNames',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.GetVarNamesResponse.FromString,
        )
    self.getOutputVarNames = channel.unary_unary(
        '/bmi.BmiService/getOutputVarNames',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.GetVarNamesResponse.FromString,
        )
    self.getTimeUnits = channel.unary_unary(
        '/bmi.BmiService/getTimeUnits',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.GetTimeUnitsResponse.FromString,
        )
    self.getTimeStep = channel.unary_unary(
        '/bmi.BmiService/getTimeStep',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.GetTimeStepResponse.FromString,
        )
    self.getCurrentTime = channel.unary_unary(
        '/bmi.BmiService/getCurrentTime',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.GetTimeResponse.FromString,
        )
    self.getStartTime = channel.unary_unary(
        '/bmi.BmiService/getStartTime',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.GetTimeResponse.FromString,
        )
    self.getEndTime = channel.unary_unary(
        '/bmi.BmiService/getEndTime',
        request_serializer=bmi__pb2.Empty.SerializeToString,
        response_deserializer=bmi__pb2.GetTimeResponse.FromString,
        )
    self.getVarGrid = channel.unary_unary(
        '/bmi.BmiService/getVarGrid',
        request_serializer=bmi__pb2.GetVarRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetVarGridResponse.FromString,
        )
    self.getVarType = channel.unary_unary(
        '/bmi.BmiService/getVarType',
        request_serializer=bmi__pb2.GetVarRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetVarTypeResponse.FromString,
        )
    self.getVarItemSize = channel.unary_unary(
        '/bmi.BmiService/getVarItemSize',
        request_serializer=bmi__pb2.GetVarRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetVarItemSizeResponse.FromString,
        )
    self.getVarUnits = channel.unary_unary(
        '/bmi.BmiService/getVarUnits',
        request_serializer=bmi__pb2.GetVarRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetVarUnitsResponse.FromString,
        )
    self.getVarNBytes = channel.unary_unary(
        '/bmi.BmiService/getVarNBytes',
        request_serializer=bmi__pb2.GetVarRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetVarNBytesResponse.FromString,
        )
    self.getValue = channel.unary_unary(
        '/bmi.BmiService/getValue',
        request_serializer=bmi__pb2.GetVarRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetValueResponse.FromString,
        )
    self.getValuePtr = channel.unary_unary(
        '/bmi.BmiService/getValuePtr',
        request_serializer=bmi__pb2.GetVarRequest.SerializeToString,
        response_deserializer=bmi__pb2.Empty.FromString,
        )
    self.getValueAtIndices = channel.unary_unary(
        '/bmi.BmiService/getValueAtIndices',
        request_serializer=bmi__pb2.GetValueAtIndicesRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetValueResponse.FromString,
        )
    self.setValue = channel.unary_unary(
        '/bmi.BmiService/setValue',
        request_serializer=bmi__pb2.SetValueRequest.SerializeToString,
        response_deserializer=bmi__pb2.Empty.FromString,
        )
    self.setValuePtr = channel.unary_unary(
        '/bmi.BmiService/setValuePtr',
        request_serializer=bmi__pb2.SetValuePtrRequest.SerializeToString,
        response_deserializer=bmi__pb2.Empty.FromString,
        )
    self.setValueAtIndices = channel.unary_unary(
        '/bmi.BmiService/setValueAtIndices',
        request_serializer=bmi__pb2.SetValueAtIndicesRequest.SerializeToString,
        response_deserializer=bmi__pb2.Empty.FromString,
        )
    self.getGridSize = channel.unary_unary(
        '/bmi.BmiService/getGridSize',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridSizeResponse.FromString,
        )
    self.getGridType = channel.unary_unary(
        '/bmi.BmiService/getGridType',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridTypeResponse.FromString,
        )
    self.getGridRank = channel.unary_unary(
        '/bmi.BmiService/getGridRank',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridRankResponse.FromString,
        )
    self.getGridShape = channel.unary_unary(
        '/bmi.BmiService/getGridShape',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridShapeResponse.FromString,
        )
    self.getGridSpacing = channel.unary_unary(
        '/bmi.BmiService/getGridSpacing',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridSpacingResponse.FromString,
        )
    self.getGridOrigin = channel.unary_unary(
        '/bmi.BmiService/getGridOrigin',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridOriginResponse.FromString,
        )
    self.getGridX = channel.unary_unary(
        '/bmi.BmiService/getGridX',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridPointsResponse.FromString,
        )
    self.getGridY = channel.unary_unary(
        '/bmi.BmiService/getGridY',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridPointsResponse.FromString,
        )
    self.getGridZ = channel.unary_unary(
        '/bmi.BmiService/getGridZ',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridPointsResponse.FromString,
        )
    self.getGridCellCount = channel.unary_unary(
        '/bmi.BmiService/getGridCellCount',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetCountResponse.FromString,
        )
    self.getGridPointCount = channel.unary_unary(
        '/bmi.BmiService/getGridPointCount',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetCountResponse.FromString,
        )
    self.getGridVertexCount = channel.unary_unary(
        '/bmi.BmiService/getGridVertexCount',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetCountResponse.FromString,
        )
    self.getGridConnectivity = channel.unary_unary(
        '/bmi.BmiService/getGridConnectivity',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridConnectivityResponse.FromString,
        )
    self.getGridOffset = channel.unary_unary(
        '/bmi.BmiService/getGridOffset',
        request_serializer=bmi__pb2.GridRequest.SerializeToString,
        response_deserializer=bmi__pb2.GetGridOffsetResponse.FromString,
        )


class BmiServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def initialize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateUntil(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateFrac(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def finalize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def runModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getComponentName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getInputVarNameCount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getOutputVarNameCount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getInputVarNames(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getOutputVarNames(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getTimeUnits(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getTimeStep(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getCurrentTime(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getStartTime(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getEndTime(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getVarGrid(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getVarType(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getVarItemSize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getVarUnits(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getVarNBytes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getValuePtr(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getValueAtIndices(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setValuePtr(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setValueAtIndices(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridSize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridType(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridRank(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridShape(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridSpacing(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridOrigin(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridX(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridY(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridZ(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridCellCount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridPointCount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridVertexCount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridConnectivity(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getGridOffset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BmiServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'initialize': grpc.unary_unary_rpc_method_handler(
          servicer.initialize,
          request_deserializer=bmi__pb2.InitializeRequest.FromString,
          response_serializer=bmi__pb2.Empty.SerializeToString,
      ),
      'update': grpc.unary_unary_rpc_method_handler(
          servicer.update,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.Empty.SerializeToString,
      ),
      'updateUntil': grpc.unary_unary_rpc_method_handler(
          servicer.updateUntil,
          request_deserializer=bmi__pb2.UpdateUntilRequest.FromString,
          response_serializer=bmi__pb2.Empty.SerializeToString,
      ),
      'updateFrac': grpc.unary_unary_rpc_method_handler(
          servicer.updateFrac,
          request_deserializer=bmi__pb2.UpdateFracRequest.FromString,
          response_serializer=bmi__pb2.Empty.SerializeToString,
      ),
      'finalize': grpc.unary_unary_rpc_method_handler(
          servicer.finalize,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.Empty.SerializeToString,
      ),
      'runModel': grpc.unary_unary_rpc_method_handler(
          servicer.runModel,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.Empty.SerializeToString,
      ),
      'getComponentName': grpc.unary_unary_rpc_method_handler(
          servicer.getComponentName,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.GetComponentNameResponse.SerializeToString,
      ),
      'getInputVarNameCount': grpc.unary_unary_rpc_method_handler(
          servicer.getInputVarNameCount,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.GetVarNameCountResponse.SerializeToString,
      ),
      'getOutputVarNameCount': grpc.unary_unary_rpc_method_handler(
          servicer.getOutputVarNameCount,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.GetVarNameCountResponse.SerializeToString,
      ),
      'getInputVarNames': grpc.unary_unary_rpc_method_handler(
          servicer.getInputVarNames,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.GetVarNamesResponse.SerializeToString,
      ),
      'getOutputVarNames': grpc.unary_unary_rpc_method_handler(
          servicer.getOutputVarNames,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.GetVarNamesResponse.SerializeToString,
      ),
      'getTimeUnits': grpc.unary_unary_rpc_method_handler(
          servicer.getTimeUnits,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.GetTimeUnitsResponse.SerializeToString,
      ),
      'getTimeStep': grpc.unary_unary_rpc_method_handler(
          servicer.getTimeStep,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.GetTimeStepResponse.SerializeToString,
      ),
      'getCurrentTime': grpc.unary_unary_rpc_method_handler(
          servicer.getCurrentTime,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.GetTimeResponse.SerializeToString,
      ),
      'getStartTime': grpc.unary_unary_rpc_method_handler(
          servicer.getStartTime,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.GetTimeResponse.SerializeToString,
      ),
      'getEndTime': grpc.unary_unary_rpc_method_handler(
          servicer.getEndTime,
          request_deserializer=bmi__pb2.Empty.FromString,
          response_serializer=bmi__pb2.GetTimeResponse.SerializeToString,
      ),
      'getVarGrid': grpc.unary_unary_rpc_method_handler(
          servicer.getVarGrid,
          request_deserializer=bmi__pb2.GetVarRequest.FromString,
          response_serializer=bmi__pb2.GetVarGridResponse.SerializeToString,
      ),
      'getVarType': grpc.unary_unary_rpc_method_handler(
          servicer.getVarType,
          request_deserializer=bmi__pb2.GetVarRequest.FromString,
          response_serializer=bmi__pb2.GetVarTypeResponse.SerializeToString,
      ),
      'getVarItemSize': grpc.unary_unary_rpc_method_handler(
          servicer.getVarItemSize,
          request_deserializer=bmi__pb2.GetVarRequest.FromString,
          response_serializer=bmi__pb2.GetVarItemSizeResponse.SerializeToString,
      ),
      'getVarUnits': grpc.unary_unary_rpc_method_handler(
          servicer.getVarUnits,
          request_deserializer=bmi__pb2.GetVarRequest.FromString,
          response_serializer=bmi__pb2.GetVarUnitsResponse.SerializeToString,
      ),
      'getVarNBytes': grpc.unary_unary_rpc_method_handler(
          servicer.getVarNBytes,
          request_deserializer=bmi__pb2.GetVarRequest.FromString,
          response_serializer=bmi__pb2.GetVarNBytesResponse.SerializeToString,
      ),
      'getValue': grpc.unary_unary_rpc_method_handler(
          servicer.getValue,
          request_deserializer=bmi__pb2.GetVarRequest.FromString,
          response_serializer=bmi__pb2.GetValueResponse.SerializeToString,
      ),
      'getValuePtr': grpc.unary_unary_rpc_method_handler(
          servicer.getValuePtr,
          request_deserializer=bmi__pb2.GetVarRequest.FromString,
          response_serializer=bmi__pb2.Empty.SerializeToString,
      ),
      'getValueAtIndices': grpc.unary_unary_rpc_method_handler(
          servicer.getValueAtIndices,
          request_deserializer=bmi__pb2.GetValueAtIndicesRequest.FromString,
          response_serializer=bmi__pb2.GetValueResponse.SerializeToString,
      ),
      'setValue': grpc.unary_unary_rpc_method_handler(
          servicer.setValue,
          request_deserializer=bmi__pb2.SetValueRequest.FromString,
          response_serializer=bmi__pb2.Empty.SerializeToString,
      ),
      'setValuePtr': grpc.unary_unary_rpc_method_handler(
          servicer.setValuePtr,
          request_deserializer=bmi__pb2.SetValuePtrRequest.FromString,
          response_serializer=bmi__pb2.Empty.SerializeToString,
      ),
      'setValueAtIndices': grpc.unary_unary_rpc_method_handler(
          servicer.setValueAtIndices,
          request_deserializer=bmi__pb2.SetValueAtIndicesRequest.FromString,
          response_serializer=bmi__pb2.Empty.SerializeToString,
      ),
      'getGridSize': grpc.unary_unary_rpc_method_handler(
          servicer.getGridSize,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridSizeResponse.SerializeToString,
      ),
      'getGridType': grpc.unary_unary_rpc_method_handler(
          servicer.getGridType,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridTypeResponse.SerializeToString,
      ),
      'getGridRank': grpc.unary_unary_rpc_method_handler(
          servicer.getGridRank,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridRankResponse.SerializeToString,
      ),
      'getGridShape': grpc.unary_unary_rpc_method_handler(
          servicer.getGridShape,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridShapeResponse.SerializeToString,
      ),
      'getGridSpacing': grpc.unary_unary_rpc_method_handler(
          servicer.getGridSpacing,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridSpacingResponse.SerializeToString,
      ),
      'getGridOrigin': grpc.unary_unary_rpc_method_handler(
          servicer.getGridOrigin,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridOriginResponse.SerializeToString,
      ),
      'getGridX': grpc.unary_unary_rpc_method_handler(
          servicer.getGridX,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridPointsResponse.SerializeToString,
      ),
      'getGridY': grpc.unary_unary_rpc_method_handler(
          servicer.getGridY,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridPointsResponse.SerializeToString,
      ),
      'getGridZ': grpc.unary_unary_rpc_method_handler(
          servicer.getGridZ,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridPointsResponse.SerializeToString,
      ),
      'getGridCellCount': grpc.unary_unary_rpc_method_handler(
          servicer.getGridCellCount,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetCountResponse.SerializeToString,
      ),
      'getGridPointCount': grpc.unary_unary_rpc_method_handler(
          servicer.getGridPointCount,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetCountResponse.SerializeToString,
      ),
      'getGridVertexCount': grpc.unary_unary_rpc_method_handler(
          servicer.getGridVertexCount,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetCountResponse.SerializeToString,
      ),
      'getGridConnectivity': grpc.unary_unary_rpc_method_handler(
          servicer.getGridConnectivity,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridConnectivityResponse.SerializeToString,
      ),
      'getGridOffset': grpc.unary_unary_rpc_method_handler(
          servicer.getGridOffset,
          request_deserializer=bmi__pb2.GridRequest.FromString,
          response_serializer=bmi__pb2.GetGridOffsetResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bmi.BmiService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
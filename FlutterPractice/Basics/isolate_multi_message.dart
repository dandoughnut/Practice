import 'dart:core';
import 'dart:io';
import 'dart:async';
import 'dart:isolate';

const filenames = [
  'D:\\book\\DataFiles\\data_file_01.txt',
  'D:\\book\\DataFiles\\data_file_02.txt',
  'D:\\book\\DataFiles\\data_file_03.txt',
];

Future<void> main() async {
  await for (final fileData in _sendAndReceive(filenames)) {
    print(fileData);
  }
}

Stream<String> _sendAndReceive(List<String> filenames) async* {
  final p = ReceivePort();
  await Isolate.spawn(_readFile, p.sendPort);
  final events = StreamIterator<dynamic>(p);
  late SendPort sendPort;

  if (await events.moveNext()) {
    sendPort = events.current;
  }
  late String message;
  for (var filename in filenames) {
    sendPort.send(filename);
    if (await events.moveNext()) {
      message = events.current;
      print('---file data : ${filename}---');
      yield message;
    }
  }
  print('-------------');
  sendPort.send(null);
  await events.cancel();
}

Future<void> _readFile(SendPort p) async {
  print('Spawned isolate started.');
  final commandPort = ReceivePort();
  p.send(commandPort.sendPort);

  await for (final message in commandPort) {
    if (message is String) {
      final contents = await File(message).readAsString();
      p.send(contents);
    } else if (message == null) {
      break;
    }
  }
  print('Spawned isolate finished.')
}
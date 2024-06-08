import 'dart:core';
import 'dart:io';
import 'dart:async';
import 'dart:isolate';

Future<void> main() async {
  final filename = 'D:\\book\\DataFiles\\data_file_01.txt';
  final receivedData = await _readInBackground(filename);
  print(receivedData);
}

Future<String> _readInBackground(String filename) async {
  final p = ReceivePort();
  await Isolate.spawn(_readFile, [p.sendPort, filename]);
  return (await p.first) as String;
}

Future<void> _readFile(List<dynamic> args) async {
  SendPort sendPort = args[0];
  String fileName = args[1];
  String fileData = await File(fileName).readAsString();
  Isolate.exit(sendPort, fileData);
}
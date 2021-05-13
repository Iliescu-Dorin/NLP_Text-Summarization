// To parse this JSON data, do
//
//     final infoCookie = infoCookieFromJson(jsonString);

import 'dart:convert';

String infoCookieToJson(InfoCookie data) => json.encode(data.toJson());

class InfoCookie {
  InfoCookie(
    this.name,
    this.f,
    this.p,
    this.r,
    this.text,
  );

  String name;
  double f;
  double p;
  double r;
  String text;

  Map<String, dynamic> toJson() => {
        "name": name,
        "f": f,
        "p": p,
        "r": r,
        "text": text,
      };
}

import 'package:flutter/material.dart';

class TodayMenuWidget extends StatelessWidget {
  const TodayMenuWidget({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    List<String> todayMenuImgUrl = [
      "lib/assets/images/cake01.jpeg",
      "lib/assets/images/cake02.jpeg",
      "lib/assets/images/cake03.jpeg",
      "lib/assets/images/dessert01.jpeg",
      "lib/assets/images/dessert02.jpeg",
    ];
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "Today\'s menu:",
            style: Theme.of(context).textTheme.titleLarge,
          ),
          GridView.count(
            physics: ScrollPhysics(),
            shrinkWrap: true,
            crossAxisCount: 3,
            children: List.generate(
              todayMenuImgUrl.length,
              (index) {
                return Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Image.asset("${todayMenuImgUrl[index]}"),
                );
              },
          ),
          )
        ],
      )
    );
  }
}
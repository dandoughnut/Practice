import 'package:cafe_app/screens/menu/coffee_menu_screen.dart';
import 'package:flutter/material.dart';
import 'package:cafe_app/widgets/banner_widget.dart';
import 'package:cafe_app/widgets/today_menu_widget.dart';

class MyHomePage extends StatelessWidget {
  const MyHomePage({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    List<String> menuItems = [
      "New",
      "Coffee",
      "Ice Cream",
      "Cake",
    ];
    List<String> bannerItemImgUrl = [
      "lib/assets/images/banner01.jpeg",
      "lib/assets/images/banner02.jpeg"
    ];
    return DefaultTabController(
      length: menuItems.length,
      child: Scaffold(
        appBar: AppBar(
          title: const Text(
            "Menu",
            style: TextStyle(color: Colors.black),
          ),
          centerTitle: true,
          backgroundColor: Colors.white,
          leading: Icon(
            Icons.home,
            color: Colors.grey,
          ),
          bottom: TabBar(
            tabs: List.generate(
              menuItems.length,
              (index) => Tab(
                text: menuItems[index],
              ),
            ),
            unselectedLabelColor: Colors.black38,
            labelColor: Colors.black,
            indicatorColor: Colors.black,
            indicatorSize: TabBarIndicatorSize.label,
            isScrollable: true,
          ),
        ),
        body: TabBarView(
            children: [
              ListView(
                children: [
                  BannerWidget(bannerItemImgUrl: bannerItemImgUrl),
                  TodayMenuWidget(),
                ],
              ),
              CoffeeMenuScreen(),
              Center(
                child: Text("Ice Cream Tab"),
              ),
              Center(
                child: Text("Cake Tab"),
              ),
            ],
        ),
      ),
    );
  }
}


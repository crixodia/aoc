import { Injectable } from '@angular/core';
import { Aoc2015Service } from './year/2015/aoc2015.service';
import { Aoc2016Service } from './year/2016/aoc2016.service';
import { Aoc2017Service } from './year/2017/aoc2017.service';
import { Aoc2018Service } from './year/2018/aoc2018.service';
import { Aoc2019Service } from './year/2019/aoc2019.service';
import { Aoc2020Service } from './year/2020/aoc2020.service';
import { Aoc2021Service } from './year/2021/aoc2021.service';
import { Aoc2022Service } from './year/2022/aoc2022.service';
import { Aoc2023Service } from './year/2023/aoc2023.service';
import { Aoc2024Service } from './year/2024/aoc2024.service';
import { Aoc2025Service } from './year/2025/aoc2025.service';

enum Year {
  Aoc2015 = 2015,
  Aoc2016 = 2016,
  Aoc2017 = 2017,
  Aoc2018 = 2018,
  Aoc2019 = 2019,
  Aoc2020 = 2020,
  Aoc2021 = 2021,
  Aoc2022 = 2022,
  Aoc2023 = 2023,
  Aoc2024 = 2024,
  Aoc2025 = 2025
}


@Injectable({
  providedIn: 'root'
})

export class SolverService {

  constructor() { }

  getFunction(year: number, day: number) {
    let aocYearService;
    switch (year) {
      case Year.Aoc2015:
        aocYearService = new Aoc2015Service();
        break;
      case Year.Aoc2016:
        aocYearService = new Aoc2016Service();
        break;
      case Year.Aoc2017:
        aocYearService = new Aoc2017Service();
        break;
      case Year.Aoc2018:
        aocYearService = new Aoc2018Service();
        break;
      case Year.Aoc2019:
        aocYearService = new Aoc2019Service();
        break;
      case Year.Aoc2020:
        aocYearService = new Aoc2020Service();
        break;
      case Year.Aoc2021:
        aocYearService = new Aoc2021Service();
        break;
      case Year.Aoc2022:
        aocYearService = new Aoc2022Service();
        break;
      case Year.Aoc2023:
        aocYearService = new Aoc2023Service();
        break;
      case Year.Aoc2024:
        aocYearService = new Aoc2024Service();
        break;
      case Year.Aoc2025:
        aocYearService = new Aoc2025Service();
        break;
      default:
        return null;
    }
    return this.getFunctionByDay(aocYearService, day);
  }

  getFunctionByDay(aocYearService: any, day: number) {
    switch (day) {
      case 1:
        return aocYearService.day1;
      case 2:
        return aocYearService.day2;
      case 3:
        return aocYearService.day3;
      case 4:
        return aocYearService.day4;
      case 5:
        return aocYearService.day5;
      case 6:
        return aocYearService.day6;
      case 7:
        return aocYearService.day7;
      case 8:
        return aocYearService.day8;
      case 9:
        return aocYearService.day9;
      case 10:
        return aocYearService.day10;
      case 11:
        return aocYearService.day11;
      case 12:
        return aocYearService.day12;
      case 13:
        return aocYearService.day13;
      case 14:
        return aocYearService.day14;
      case 15:
        return aocYearService.day15;
      case 16:
        return aocYearService.day16;
      case 17:
        return aocYearService.day17;
      case 18:
        return aocYearService.day18;
      case 19:
        return aocYearService.day19;
      case 20:
        return aocYearService.day20;
      case 21:
        return aocYearService.day21;
      case 22:
        return aocYearService.day22;
      case 23:
        return aocYearService.day23;
      case 24:
        return aocYearService.day24;
      case 25:
        return aocYearService.day25;
      default:
        return null;
    }
  }
}

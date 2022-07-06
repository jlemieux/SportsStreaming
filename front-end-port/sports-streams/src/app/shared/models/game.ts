export interface Game {
  team1: string;
  team2: string;
  score: string;
  time: string;
  link: string;
};

export interface BaseballGame extends Game {
  id: string;
};

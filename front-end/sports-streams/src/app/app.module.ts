import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { SportChoicesComponent } from './header/sport-choices/sport-choices.component';
import { SportChoiceComponent } from './header/sport-choices/sport-choice/sport-choice.component';
import { ContentComponent } from './content/content.component';
import { GameChoicesComponent } from './content/game-choices/game-choices.component';
import { GameChoiceComponent } from './content/game-choices/game-choice/game-choice.component';
import { TeamNameComponent } from './content/game-choices/game-choice/team-name/team-name.component';
import { ScoreAndTimeComponent } from './content/game-choices/game-choice/score-and-time/score-and-time.component';
import { WatchButtonComponent } from './content/game-choices/game-choice/watch-button/watch-button.component';
import { NoGamesFoundComponent } from './content/game-choices/no-games-found/no-games-found.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    SportChoicesComponent,
    SportChoiceComponent,
    ContentComponent,
    GameChoicesComponent,
    GameChoiceComponent,
    TeamNameComponent,
    ScoreAndTimeComponent,
    WatchButtonComponent,
    NoGamesFoundComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

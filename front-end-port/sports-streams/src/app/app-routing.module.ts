import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ContainerComponent } from './container/container.component';
import { BaseballStreamComponent } from './shared/baseball-stream/baseball-stream.component';

const routes: Routes = [
  { path: '', component: ContainerComponent, pathMatch: 'full' },
  { path: 'baseball-stream', component: BaseballStreamComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

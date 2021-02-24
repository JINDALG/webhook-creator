import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { WebhookDetailComponent } from './webhook-detail/webhook-detail.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'webhook-detail/:id', component: WebhookDetailComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}

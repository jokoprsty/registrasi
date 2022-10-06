import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CounterComponent } from './components/counter/counter/counter.component';

const routes: Routes = [
  {
    path:"mahasiswa", loadChildren: ()=> import("./components/mahasiswa/mahasiswa.module").then(m => m.MahasiswaModule),
    
  },
  {
    path:"counter", component: CounterComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

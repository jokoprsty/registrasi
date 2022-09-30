import { NgModule } from "@angular/core";
import { MahasiswaRoutingModule } from "./mahasiswa-routing.module";
import { MahasiswaComponent } from "./mahasiswa/mahasiswa.component";

@NgModule({
    declarations:[
        MahasiswaComponent,
    ],
    imports: [
        MahasiswaRoutingModule,
    ]
   
})

export class MahasiswaModule{
    
}
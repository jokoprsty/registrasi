import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { MahasiswaRoutingModule } from "./mahasiswa-routing.module";
import { MahasiswaComponent } from "./mahasiswa/mahasiswa.component";

@NgModule({
    declarations:[
        MahasiswaComponent,
    ],
    imports: [
        MahasiswaRoutingModule,
        CommonModule,
    ]
   
})

export class MahasiswaModule{
    
}
import { Component, OnInit } from '@angular/core';
import { Mahasiswa } from 'src/app/interfaces/mahasiswa';
import { MahasiswaService } from 'src/app/services/mahasiswa/mahasiswa.service';

@Component({
  selector: 'app-mahasiswa',
  templateUrl: './mahasiswa.component.html',
  styleUrls: ['./mahasiswa.component.scss']
})
export class MahasiswaComponent implements OnInit {

  public dataMahasiswa?: Mahasiswa;

  constructor(private mahasiswa: MahasiswaService) { }

  ngOnInit(): void {
    this.mahasiswa.getMahasiswa().subscribe(data => {
      this.dataMahasiswa = data;
      console.log(this.dataMahasiswa);
    } 
    );
  }

}

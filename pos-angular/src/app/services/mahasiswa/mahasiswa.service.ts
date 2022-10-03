import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Mahasiswa } from 'src/app/interfaces/mahasiswa';

@Injectable({
  providedIn: 'root'
})
export class MahasiswaService {

  constructor(private http:HttpClient) { }

  getMahasiswa(): Observable<Mahasiswa>{
    let url = `http://127.0.0.1:8000/mahasiswa/?format=json`;
    return this.http.get<Mahasiswa>(url);
  }

}

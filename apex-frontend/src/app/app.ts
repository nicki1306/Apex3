import { Component } from '@angular/core';
import { VehicleListComponent } from './components/vehicle-list/vehicle-list';
import{ VehicleFormComponent } from './components/vehicle-form/vehicle-form.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ VehicleListComponent, VehicleFormComponent],
  template: `
    <main>
      <h1>¡Bienvenida a Apex Angular!</h1>
      <app-vehicle-form></app-vehicle-form>
      <app-vehicle-list></app-vehicle-list> </main>
  `
})
export class AppComponent { }
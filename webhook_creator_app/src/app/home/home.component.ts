import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Webhook } from 'src/core/models/webhook.model';
import { WebhookService } from 'src/core/services/webhook.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  isCreateFormOpened = false;
  webHookList: Array<Webhook> = [];

  createWebhookForm: FormGroup = this.formBuilder.group({
    key: ['', Validators.required],
  });

  constructor(
    private webhookService: WebhookService,
    private formBuilder: FormBuilder
  ) {}

  onWebhookFormSubmit() {
    if (this.createWebhookForm.invalid) {
      alert('Please fill all values.');
      return;
    }

    const data = {
      key: this.createWebhookForm.value.key,
    };

    this.webhookService.createWebHook(data).subscribe({
      next: (res: any) => {
        if (res.id) {
          this.closeDialog();
          this.getWebhooksList();
          alert('Created Successfully!');
        }
      },
      error: () => {
        this.displayError();
      },
    });
  }

  getWebhooksList() {
    this.webhookService.getWebHooksList().subscribe({
      next: (res) => {
        this.webHookList = res;
      },
      error: () => {
        this.displayError();
      },
    });
  }

  displayError() {
    alert('Some Error Occured! Check Console');
  }

  handleCreateButton() {
    this.isCreateFormOpened = true;
  }

  closeDialog() {
    this.isCreateFormOpened = false;
  }

  ngOnInit(): void {
    this.getWebhooksList();
  }
}

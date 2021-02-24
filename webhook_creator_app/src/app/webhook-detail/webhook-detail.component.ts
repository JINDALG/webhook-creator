import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Webhook } from 'src/core/models/webhook.model';
import { WebhookService } from 'src/core/services/webhook.service';

@Component({
  selector: 'app-webhook-detail',
  templateUrl: './webhook-detail.component.html',
  styleUrls: ['./webhook-detail.component.scss'],
})
export class WebhookDetailComponent implements OnInit {
  webhookId: number = 0;
  webhookDetail?: Webhook;

  constructor(
    private activatedRoute: ActivatedRoute,
    private webhookService: WebhookService
  ) {}

  getWebhookDetails() {
    if (!this.webhookId) {
      return;
    }

    this.webhookService.getWebhookDetails(this.webhookId).subscribe({
      next: (res: any) => {
        this.webhookDetail = res;
      },
      error: () => {
        alert('Some Error Occured, Check Console!');
      },
    });
  }

  handleQueryParams(params: any) {
    if (!params.id) {
      return;
    }

    this.webhookId = Number(params.id);
    this.getWebhookDetails();
  }

  ngOnInit(): void {
    this.activatedRoute.params.subscribe((params) => {
      console.log(params);
      this.handleQueryParams(params);
    });
  }
}

#include "lists.h"
/**
* get_prev_node - helper function to get previous node
* @head: pointer to the head
* @back: pointer pointing to back of list
* Return: pointer to previous pointer to back
*/
listint_t *get_prev_node(listint_t *head, listint_t *back)
{
	if ((head == back) || head->next == back)
	{
		return (head);
	}
	while (head->next != back)
	{
		head = head->next;
	}
	return (head);
}

/**
 * is_palindrome - functiont to verify if a linked list is a palindrome
 * @head: pointer to the head
 * Return: 0 if its not a palindrome and 1 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *back = NULL;
	listint_t *front = *head;
	listint_t *tmp = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (tmp->next != NULL)
	{
		tmp = tmp->next;
	}
	back = tmp;
	while (front != back)
	{
		if (front->n != back->n)
		{
			return (0);
		}
		front = front->next;
		back = get_prev_node(front, back);
	}
	return (1);
}
